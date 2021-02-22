from rest_framework import routers

from .views import AvatarViewSet


app_name = 'rest_avatar'

router = routers.DefaultRouter()
router.register('', AvatarViewSet, basename='avatar')


urlpatterns = router.urls
