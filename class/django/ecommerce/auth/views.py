from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.crypto import get_random_string


from .models import User
from .serializers import (
    ChangePasswordSerializer,
    LoginSerializer,
    ForgotPasswordSerializer,
    VerifyOtpSerializer,
)
from .utils import send_user_mail


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get("user")

        refresh = RefreshToken.for_user(user)
        response_data = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
            },
        }

        return Response({"detail": "Login successful", "data": response_data})


class ChangePasswordView(generics.GenericAPIView):
    serializer_class = ChangePasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        user.set_password(serializer.validated_data["new_password"])
        user.save()
        return Response({"detail": "Password changed successfully."})


class ForgotPasswordView(generics.GenericAPIView):
    serializer_class = ForgotPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]

        otp = get_random_string(length=6, allowed_chars="0123456789")
        message = f"Your OTP for password reset is: {otp}"

        user.otp = otp
        user.save()

        send_user_mail("Password Reset OTP", [user.email], message)

        return Response({"detail": "Password reset link sent to your email."})


class VerifyOtpView(generics.GenericAPIView):
    serializer_class = VerifyOtpSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response({"detail": "OTP verified successfully."})
