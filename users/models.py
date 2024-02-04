from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from .manager import UserManager


# Create your models here.
class User(AbstractUser,PermissionsMixin):
    GENDER_CHOICES = [
        ("M", _("Male")),
        ("F", _("Female")),
    ]

    name = models.CharField(max_length=255, verbose_name = _("Username"))
    gender = models.CharField(max_length = 10, choices=GENDER_CHOICES,verbose_name=_("Gender"))
    email = models.EmailField(max_length=255,unique=True,verbose_name=_("Email address"))
    phone_number = PhoneNumberField(max_length=15,unique=True, verbose_name=_("Mobile Number"))
    instagram = models.CharField(max_length=255, unique=True,  verbose_name=_("Instagram"))
    location = models.CharField(max_length=255, verbose_name=_("Location"))
    category = models.JSONField(verbose_name=_("Category"))
    experience = models.IntegerField(verbose_name=_("Experience"))
    unique_code = models.CharField(max_length=100,unique=True, editable=False)
    notification = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    
    username = None
    
    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ["name"]
    
    objects = UserManager()
    
    
    def __str__(self):
        return self.name
    

class CategoryName(models.Model):
    name = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.name
    
    
    
    