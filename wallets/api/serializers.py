from rest_framework import serializers

from users.models import User
from reviews.models import Wallets


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username',)


class WalletsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wallets
        fields = ('id', 'balance')

    def create(self, validated_data):
        author = self.context['request'].user
        wallets = Wallets.objects.create(author=author, **validated_data)
        return wallets
