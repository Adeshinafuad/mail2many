import email
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here
class User(AbstractBaseUser):
    username = None
    email = models.EmailField(('email address'), unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
class Upload(models.Model):
    mail_title = models.TextField(max_length=80)
    mail_text = models.TextField(max_length=320)
    upload_description = models.CharField(max_length=80)
    timestamp = models.DateTimeField(auto_now_add=True)
    spreadsheet = models.FileField(blank=False,null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    sender_email = models.EmailField(blank=False,null=False)
    
    def __str__(self):
        return self.mail_title
    
class Receipient(models.Model):
    data = models.ForeignKey(Upload,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    reciever_email = models.EmailField(blank=False,null=False)
    
    def __str__(self):
        return self.name
    
    
    
    
    
    
    