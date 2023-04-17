from django.contrib.auth.models import User
from rest_framework import viewsets, generics

from users import serializers
from users.serializers import UserSerializer
from uzum import permissions, views
from uzum.permissions import IsOwner


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUserOrReadOnly, IsOwner)


class LoginView(views.TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.LoginSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.RegisterSerializer