from rest_framework import serializers
from .models import User
from django.db.utils import IntegrityError
from rest_framework.exceptions import ValidationError

class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        user  = User(username=username,email=email)
        user.set_password(password)
        try:
            user.save()
        except IntegrityError:
            raise ValidationError('Username already exists!')
        return user
    
class UserLoginSerilizer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()