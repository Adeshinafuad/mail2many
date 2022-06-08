from datetime import datetime, timedelta, date
from django.db import models
from common.models import BaseModel
from django.dispatch import receiver
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
import uuid
from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _






class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user




    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(email, password, **extra_fields)



class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        unique=True, help_text="A confirmation message would be sent to your Email"
    )
    business_name = models.CharField(max_length=100, null=True, blank=True)

    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=300, null=True, blank=True)
    country = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=300, null=True, blank=True)

    # last_login = models.DateTimeField(auto_now_add=True)



    __account_type = ( 
          ('personal', 'personal'),
          ('busines', 'busines'),          
    )
    account_type  = models.CharField(max_length=100, choices= __account_type)




    class Meta(object):
        unique_together = ("email",)

    USERNAME_FIELD = "email"
    objects = UserManager()

    REQUIRED_FIELDS = ["first_name", "last_name"]

    def full_name(self):
        return "{} {} {}".format(self.first_name, self.last_name, self.email) if self.account_type == "personal" else  "{} {}".format(self.business_name, self.email)
    
    def my_email(self):
        return "{}".format(self.email)

    def __str__(self):
        return str(self.my_email())
        # return 'hello'
    @property
    def user_id(self):
        return self.id.__str__()




