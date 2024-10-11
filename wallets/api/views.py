from rest_framework import viewsets, status
from djoser.views import UserViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db import transaction
from rest_framework.permissions import IsAuthenticated

from users.models import User
from reviews.models import Wallets
from .serializers import UserSerializer, WalletsSerializer


class UserViewSet(UserViewSet):
    """Вьюсет для пользователей и авторов."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class WelltsViewSet(viewsets.ModelViewSet):
    """Вьюсет для кошелька."""
    queryset = Wallets.objects.all()
    serializer_class = WalletsSerializer
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['post'])
    def operation(self, request, pk=None):
        wallet = self.get_object()
        operation_type = request.data.get('operationType')
        amount = request.data.get('amount')

        if wallet.author != request.user:
            return Response({'У вас нет прав для изменения этого кошелька.'},
                            status=status.HTTP_403_FORBIDDEN)

        if amount is None or amount <= 0:
            return Response({'Сумма должна быть положительной.'},
                            status=status.HTTP_400_BAD_REQUEST)

        if operation_type not in ['DEPOSIT', 'WITHDRAW']:
            return Response({'Неизвестный тип операции.'},
                            status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            wallet.refresh_from_db()

            if operation_type == 'DEPOSIT':
                wallet.balance += amount
            elif operation_type == 'WITHDRAW':
                if wallet.balance >= amount:
                    wallet.balance -= amount
                else:
                    return Response(
                        {f'Недостачно средств. Ваш баланс {wallet.balance}.'},
                        status=status.HTTP_400_BAD_REQUEST)
            wallet.save()
        return Response({'Баланс': wallet.balance},
                        status=status.HTTP_200_OK)
