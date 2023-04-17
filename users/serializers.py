from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers, validators
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'first_name', 'last_name']


class LoginSerializer(TokenObtainPairSerializer):

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    @classmethod
    def get_token(cls, user):
        token = super(LoginSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,
                                   validators=[validators.UniqueValidator(queryset=User.objects.all())])
    # phone = serializers.CharField(max_length=13, required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            # phone=validated_data['phone'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


# from django.contrib.auth.hashers import make_password
# from django.contrib.auth.models import User
# from django.db.models import CharField
# from rest_framework.exceptions import ValidationError
# from rest_framework.serializers import ModelSerializer
#
#
# class CreateUserProfileSerializer(ModelSerializer):
#     password = CharField(max_length=255, write_only=True)
#     confirm_password = CharField(max_length=255, write_only=True)
#
#     # def create(self, validated_data):
#     #     user = User.objects.create(**validated_data)
#     #     UserProfile.objects.create(user=user)
#     #     return user
#
#     def validate(self, attrs):
#         confirm_password = attrs.pop('confirm_password')
#         password = attrs.get('password')
#         if confirm_password != password:
#             raise ValidationError("Passwords didn't match.")
#         attrs['password'] = make_password(password)
#         validated_data = super().validate(attrs)
#         return validated_data
#
#     @staticmethod
#     def validate_password(password):
#         if len(password) < 8:
#             raise ValidationError("Password is too short.")
#         return password
#
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'password', 'confirm_password')
#
