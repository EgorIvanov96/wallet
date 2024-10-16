from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import UserViewSet, WelltsViewSet


app_name = 'api'

router = DefaultRouter()

router.register(r'users', UserViewSet, basename='users')
router.register(r'wallets', WelltsViewSet, basename='WelltsViewSet')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.jwt')),
]
