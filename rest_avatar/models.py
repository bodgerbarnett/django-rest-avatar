from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


def avatar_file_path(instance, filename):
    return 'avatars/{}/{}'.format(instance.user.id, filename)


class Avatar(models.Model):
    user = models.ForeignKey(
        User, related_name='avatars', on_delete=models.CASCADE
    )
    is_primary = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to=avatar_file_path)

    def set_primary(self):
        self.user.avatars.update(is_primary=False)
        self.is_primary = True
        self.save()
