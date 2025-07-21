from django.urls import path

from .views import (
    LoginView,
    ChangePasswordView,
    ForgotPasswordView,
    VerifyOtpView,
)


urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("change-password/", ChangePasswordView.as_view(), name="change_password"),
    path("forgot-password/", ForgotPasswordView.as_view(), name="forgot_password"),
    path("verify-otp/", VerifyOtpView.as_view(), name="verify_otp"),
]
