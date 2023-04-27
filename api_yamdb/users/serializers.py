from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.RegexField(
        validators=[UniqueValidator(queryset=User.objects.all())],
        max_length=150,
        regex=r'^[a-zA-Z0-9@.+-_]+$'
    )
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())],
        max_length=254,
    )
    first_name = serializers.CharField(
        max_length=150,
        required=False
    )
    last_name = serializers.CharField(
        max_length=150,
        required=False
    )

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'bio', 'role'
        )


class UserEditSerializer(serializers.ModelSerializer):
    username = serializers.RegexField(
        validators=[UniqueValidator(queryset=User.objects.all())],
        max_length=150,
        regex=r'^[a-zA-Z0-9@.+-_]+$'
    )

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'bio', 'role'
        )
        read_only_fields = ('role',)


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True,
        max_length=254,
    )
    username = serializers.RegexField(
        required=True,
        max_length=150,
        regex=r'^[a-zA-Z0-9@.+-_]+$'
    )

    def validate_username(self, value):
        if value.lower() == 'me':
            raise serializers.ValidationError('Придумайте другой username!')
        return value


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)
