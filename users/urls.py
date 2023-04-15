from django.urls import path, include

from users.views import UserCreateApiView

urlpatterns = [
    path('', include('rest_framework.urls')),
    path('register/', UserCreateApiView.as_view(), name='register')
]
