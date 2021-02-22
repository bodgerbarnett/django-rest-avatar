from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import AvatarSerializer


class AvatarViewSet(viewsets.ModelViewSet):
    serializer_class = AvatarSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.avatars.all()

    def perform_create(self, serializer):
        avatar = serializer.save(user=self.request.user)
        avatar.set_primary()

    @action(['patch'], detail=True)
    def set_primary(self, request, *args, **kwargs):
        self.get_object().set_primary()
        return Response(status=status.HTTP_204_NO_CONTENT)
