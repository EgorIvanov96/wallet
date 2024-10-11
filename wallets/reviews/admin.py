from django.contrib import admin

from .models import Wallets

admin.site.register(Wallets)
admin.site.empty_value_display = 'Не задано'
