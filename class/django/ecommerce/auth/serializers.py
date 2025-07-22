from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "first_name",
            "last_name",
            "profilepic",
            "phone_number",
            "password",
        ]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            password=validated_data["password"],
            profilepic=validated_data.get("profilepic"),
            phone_number=validated_data.get("phone_number"),
        )

        # User.objects.create_user(**validated_data)

        return user

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        # password = validated_data.get("password")
        # if password:
        #     instance.set_password(password)

        instance.save()
        return instance


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        if not username or not password:
            raise serializers.ValidationError("Username and password are required.")

        user = User.objects.filter(username=username).first()
        if user is None or not user.check_password(password):
            raise serializers.ValidationError("Invalid credentials.")

        attrs["user"] = user
        return attrs


class ChangePasswordSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True)

    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is incorrect.")
        return value

    def validate_new_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError(
                "New password must be at least 8 characters long."
            )
        return value

    def validate(self, attrs):

        user = attrs.get("user")
        if not user:
            raise serializers.ValidationError(
                "User must be provided for password change."
            )
        if not user.is_authenticated:
            raise serializers.ValidationError(
                "User must be authenticated to change password."
            )
        old_password = attrs.get("old_password")
        if not user.check_password(old_password):
            raise serializers.ValidationError("Old password is incorrect.")

        return attrs


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    # def validate_email(self, value):
    #     if not User.objects.filter(email=value).exists():
    #         raise serializers.ValidationError("No user found with this email address.")
    #     return value

    def validate(self, attrs):

        email = attrs.get("email")
        if not email:
            raise serializers.ValidationError("Email is required for password reset.")
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError("No user found with this email address.")
        attrs["user"] = User.objects.get(email=email)

        return attrs


class VerifyOtpSerializer(serializers.Serializer):
    otp = serializers.CharField(required=True, max_length=6)
    email = serializers.EmailField(required=True)

    def validate(self, attrs):
        otp = attrs.get("otp")
        email = attrs.get("email")
        if not otp or not email:
            raise serializers.ValidationError("OTP and email are required.")

        user = User.objects.filter(email=email).first()
        if not user:
            raise serializers.ValidationError("No user found with this email address.")

        if user.otp != otp:
            raise serializers.ValidationError("Invalid OTP provided.")
        attrs["user"] = user
        return attrs
