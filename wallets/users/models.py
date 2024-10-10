from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator


class User(AbstractUser):
    """Модель пользователя."""

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    email = models.EmailField(
        unique=True,
        max_length=150,
        verbose_name='e-mail',
        help_text='Укажите свой e-mail'
    )
    username = models.CharField(
        max_length=150,
        verbose_name='Имя пользователя',
        help_text='Укажите имя пользователя',
        unique=True,
        validators=[
            RegexValidator(
                r'^[\w.@+-]+\Z',
                'Поле username содержит недопустимые символы'
            )
        ]
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ['username']

    def __str__(self):
        return self.username
