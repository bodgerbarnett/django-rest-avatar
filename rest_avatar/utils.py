from django.conf import settings

from .models import Avatar


def get_avatar_url(request, user):
    try:
        url = user.avatars.get(is_primary=True).avatar.url
    except Avatar.DoesNotExist:
        # TODO make the image a setting
        url = '{}images/player.png'.format(settings.STATIC_URL)

    return request.build_absolute_uri(url)
