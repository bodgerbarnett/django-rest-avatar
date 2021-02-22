from rest_framework import routers

from .views import AvatarViewSet


router = routers.DefaultRouter()
router.register('', AvatarViewSet, basename='avatar')


urlpatterns = router.urls
