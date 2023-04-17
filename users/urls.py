from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from users.views import LoginView, RegisterView

urlpatterns = [
    path('', include('rest_framework.urls')),

    path(r'^login/', LoginView.as_view(), name='auth_login'),
    path(r'^register/', RegisterView.as_view(), name='auth_register'),
    path(r'^login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]