from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','username','first_name','last_name','profile_pic','phone_number','pasword']

    def create(self, validated_data):
        user  = User.objects.crete_user(
            email = validated_data['email'],
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            profile_pic = validated_data.get('profile_pic'),
            phone_number = validated_data.get('phone_number')
        )
        return user
        
    def update(self, instance,validated_data):
        for key,value in validated_data.items():
            setattr(instance,key,value)

        instance.save()
        return instance
    
class ChangePasswordSerializer(serializers.Serializer):
    user = serializers.HiddenField(default = serializers.CurrentUserDefault())
    old_password = serializers.CharField(required=True,write_only=True)
    new_password = serializers.CharField(required=True,write_only=True)

    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError("Password is incorrect.")
        return value
    
    def validate_new_password(self, value):
        if len(value) < 8 :
            raise serializers.ValidationError("Password must be 8 characters long.")
        return value
    
    def validate(self, attrs):
        user = attrs.get("user")
        if not user:
            raise serializers.ValidationError("User not provided.")
        if not user.is_authenticated():
            raise serializers.ValidationError("User is not authenticated.")
        
        old_password = attrs.get("old_password")
        if not user.check_password(old_password):
            raise serializers.ValidationError("Old password is incorrect.")

        return attrs
    
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

class ForgetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate_email(self,value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Provide registered email")
        return value
    
    def validate(self,attrs):
        email = attrs.get("email")
        if not email:
            raise serializers.ValidationError("Provide an email")
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Provide registered email")
        attrs["user"]=User.objects.get(email=email)
        return attrs
    
class VerifyOtpSerializer(serializers.Serializer):
    otp = serializers.CharField(max_length=6,required=True)
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