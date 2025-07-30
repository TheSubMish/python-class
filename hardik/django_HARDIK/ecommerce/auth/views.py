from django.shortcuts import render

from rest_framework import generics,permissions
from rest_framework.response import Response
from django.utils.crypto import get_random_string

from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import ChangePasswordSerializer, LoginSerializer, UserSerializer,ForgetPasswordSerializer,VerifyOtpSerializer
from .models import User
from .utils import send_user_mail

# Create your views here.

class ChangePasswordAPI(generics.GenericAPIView):
    serializer_class = ChangePasswordSerializer

    def post(self,request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception =True)
        user = request.user
        user.set_password(serializer.validated_data["new_password"])
        user.save()
        return Response("New Password set.")
    
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
                "email": user.email,
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
            },
        }

        return Response({"detail": "Login successful", "data": response_data})
    
class ForgetPasswordView(generics.GenericAPIView):
    serializer_class = ForgetPasswordSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception =True)
        user = serializer.validated_data["user"]
        
        otp = get_random_string(length=6,allowed_chars="0123456789")
        user.otp = otp
        user.save()
        message = f"OTP:{otp}"
        send_user_mail("Password reset OTP",[user.email],message)

        return Response({"details":"OTP sent"})
    
class VerifyOtpView(generics.GenericAPIView):
    serializer_class = VerifyOtpSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response({"detail": "OTP verified successfully."})
