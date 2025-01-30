from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from dj_rest_auth.views import LoginView, LogoutView
from .views import TestView, AdminView

urlpatterns = [
    path('test/', TestView.as_view(), name='test'),
    path("test-admin/", AdminView.as_view(), name="test_admin"),
    # path('auth/login/', LoginView.as_view(), name='rest_login'),
    # path('auth/logout/', LogoutView.as_view(), name='rest_logout'),
    # path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]