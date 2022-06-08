from django.contrib import admin
from .models import EmailListUpload, EmailReceipientRelationship

# Register your models here.
admin.site.register(EmailListUpload)
admin.site.register(EmailReceipientRelationship)
