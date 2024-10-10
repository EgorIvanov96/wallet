from django.contrib import admin

from .models import User

admin.site.register(User)
admin.site.empty_value_display = 'Не задано'
