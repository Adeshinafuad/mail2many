from django.db import models
from django.utils.translation import ugettext_lazy as _
from common.models import BaseModel
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

from .managers import CustomUserManager


class CustomUser(BaseModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    business_name = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=300, null=True, blank=True)
    country = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=300, null=True, blank=True)

    __account_type = ( 
          ('personal', 'personal'),
          ('busines', 'busines'),          
    )
    account_type  = models.CharField(max_length=100, choices= __account_type)


    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

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

