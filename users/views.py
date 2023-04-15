from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from users.serializers import CreateUserProfileSerializer


class UserCreateApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserProfileSerializer
    permission_classes = (IsAuthenticated,)
