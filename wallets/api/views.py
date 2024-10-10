from rest_framework import viewsets
from djoser.views import UserViewSet

from users.models import User
from .serializers import UserSerializer


class UserViewSet(UserViewSet):
    """Вьюсет для пользователей и авторов."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
