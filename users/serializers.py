from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db.models import CharField
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer


class CreateUserProfileSerializer(ModelSerializer):
    password = CharField(max_length=255, write_only=True)
    confirm_password = CharField(max_length=255, write_only=True)

    # def create(self, validated_data):
    #     user = User.objects.create(**validated_data)
    #     UserProfile.objects.create(user=user)
    #     return user

    def validate(self, attrs):
        confirm_password = attrs.pop('confirm_password')
        password = attrs.get('password')
        if confirm_password != password:
            raise ValidationError("Passwords didn't match.")
        attrs['password'] = make_password(password)
        validated_data = super().validate(attrs)
        return validated_data

    @staticmethod
    def validate_password(password):
        if len(password) < 8:
            raise ValidationError("Password is too short.")
        return password

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'confirm_password')

