from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenBlacklistView

from users.views import LoginView, RegisterView

router = routers.DefaultRouter()

urlpatterns = [
    re_path(r'^login/', LoginView.as_view(), name='auth_login'),
    re_path(r'^login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'^register/', RegisterView.as_view(), name='auth_register'),

    path('', include(router.urls)),
]