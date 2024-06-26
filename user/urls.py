from django.contrib.auth.views import LogoutView
from django.urls import path

from user.views import UserRegisterView, UserVerificationView, UserLoginView, RestorePasswordUserView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path(
        'email/verification/<str:token>/',
        UserVerificationView.as_view(),
        name='verification-email'
    ),
    path(
        'login/',
        UserLoginView.as_view(),
        name='login'
    ),
    path(
        'logout/',
        LogoutView.as_view(),
        name='logout'
    ),
    path(
        'restore-password/',
        RestorePasswordUserView.as_view(),
        name="restore-password",
    ),
]
