from django.db import models
import uuid

from users.models import User


class Wallets(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    author = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    balance = models.FloatField(
        default=0.0,
        verbose_name='Баланс',
    )

    class Meta:
        verbose_name = 'Кошелек'
        verbose_name_plural = 'кошельки'

    def __str__(self):
        return f'Кошелек {self.author}; Баланс: {self.balance}'
