from django.contrib import admin
from .models import User, Upload, Receipient

# Register your models here.
admin.site.register(User)
admin.site.register(Upload)
admin.site.register(Receipient)