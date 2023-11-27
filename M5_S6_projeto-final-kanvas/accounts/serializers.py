from rest_framework import serializers
from accounts.models import Account
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "id",
            "username",
            "password",
            "email",
            "is_superuser",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict) -> Account:
        return Account.objects.create_user(**validated_data)

    class CustomJWTSerializer(TokenObtainPairSerializer):
        @classmethod
        def get_token(cls, user):
            token = super().get_token(user)
            token["is_superuser"] = user.is_superuser
            return token
