from rest_framework import serializers

from django.contrib.auth import get_user_model
from django.core.files.images import get_image_dimensions
from django.template.defaultfilters import filesizeformat

from .conf import settings
from .models import Avatar


User = get_user_model()


class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avatar
        fields = ['id', 'avatar']

    def validate_avatar(self, avatar):
        if avatar.size > settings.AVATAR_MAX_SIZE:
            raise serializers.ValidationError(
                'Your file is too big ({}), the maximum allowed size is {}'.format(
                    filesizeformat(avatar.size),
                    filesizeformat(settings.AVATAR_MAX_SIZE)
                )
            )

        width, height = get_image_dimensions(avatar)

        if width < 200 or height < 200:
            raise serializers.ValidationError(
                'Logo must be at least 200px x 200px'
            )

        return avatar
