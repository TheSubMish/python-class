from django.db import models

from django.contrib.auth.models import(AbstractBaseUser,BaseUserManager,PermissionsMixin)

from .utils import image_validate
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,email,username,password=None,**extra_fields):
        if not email:
            raise ValueError("Provide Email")
        
        email = self.normalize_email(email)
        user = self.model(username=username,email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,username,first_name,last_name,password=None):
        user = self.create_user(email,username,first_name=first_name,last_name=last_name,password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user

class RoleType(models.TextChoices):
    ADMIN = 'admin','Admin'
    CUSTOMER = 'customer','Customer'

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50,unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='profile',blank=True,null=True,validators=[image_validate])
    phone_number = models.CharField(max_length=20,null=True,blank=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
    role = models.CharField(max_length=10,choices=RoleType.choices,default=RoleType.CUSTOMER)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name','last_name']

    def __str__(self):
        return self.first_name
    