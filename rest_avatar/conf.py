from django.conf import settings

from appconf import AppConf


class RestAvatarConf(AppConf):
    MAX_SIZE = 1024 * 1024
