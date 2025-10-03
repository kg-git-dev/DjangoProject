from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': True}
        }

    def create(self, validated_data):
        """Hashes the password when creating a new user."""
        validated_data['password'] = make_password(validated_data['password'])
        user = super().create(validated_data)
        return user

    def update(self, instance, validated_data):
        """Hashes the password if it's being updated."""
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        user = super().update(instance, validated_data)
        return user
