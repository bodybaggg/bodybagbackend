from django.contrib.auth.models import BaseUserManager
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _



class UserManager(BaseUserManager):
    def email_validator(self,email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("Please enter a valid email address"))
    
    def create_user(self, name,gender,email,phone_number,instagram,location,password,category,experience,**extra_fields):
        
        
        if email:
            email=self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("an email address is required"))
        
        if not name:
            raise ValueError(_("an name is required"))
        
        if not gender:
            raise ValueError(_("an gender is required"))
        
        if not phone_number:
            raise ValueError(_("an phone_number is required"))
        
        if not instagram:
            raise ValueError(_("an name is required"))
        
        if not location:
            raise ValueError(_("an location is required"))
        
        if not category:
            raise ValueError(_("an category is required"))
        
        if not experience:
            raise ValueError(_("an experience is required"))
        
        user = self.model(name=name,gender=gender,email=email,phone_number=phone_number,instagram=instagram, location=location, category=category,experience=experience,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
                   
                   
    def create_superuser(self,name, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_verified", True)
        extra_fields.setdefault("gender", "M")
        extra_fields.setdefault("instagram", "admin")
        extra_fields.setdefault("phone_number", "+918606257889")
        extra_fields.setdefault("location", "Kochi")
        extra_fields.setdefault("category", ["rapper"])
        extra_fields.setdefault("experience", 1)
        extra_fields.setdefault("unique_code","H00")
        
        
        

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("is_staff must be true for admin user"))

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("is_superuser must be true for admin user"))

        user = self.create_user(
            name=name,
            email=email,
            password=password,
            **extra_fields
        )
        user.save(using=self._db)
        return user