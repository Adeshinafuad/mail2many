from common import status
from django.db import models
from common.models import BaseModel
from users.models import CustomUser
    


def email_upload_status_file_path(instance, filename):
    return f'payroll-validation-/{filename}'
class EmailListUpload(BaseModel):
    # uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    mail_title = models.TextField(max_length=80)
    mail_text = models.TextField(max_length=320)
    upload_description = models.CharField(max_length=80)
    timestamp = models.DateTimeField(auto_now_add=True)
    spreadsheet = models.FileField(blank=False,null=False)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    sender_email = models.EmailField(blank=False,null=False)

    success_count = models.IntegerField(default=0, editable=False)
    success_file = models.FileField(null=True, blank=True, editable=False,
                                    upload_to=email_upload_status_file_path)
    failure_count = models.IntegerField(default=0, editable=False)
    failure_file = models.FileField(null=True, blank=True, editable=False,
                                    upload_to=email_upload_status_file_path)

    status = models.CharField(max_length=30, editable=False,
                              default=status.UPLOAD_PROCESSING_STATUS,
                              choices=status.UPLOAD_STATUSES)

    def __str__(self):
        return self.mail_title
    
class EmailReceipientRelationship(BaseModel):
    email_upload_list = models.ForeignKey(EmailListUpload,on_delete=models.CASCADE)
    recipient_name = models.CharField(max_length=50)
    reciever_email = models.EmailField(blank=False,null=False)
    status = models.CharField(max_length=30, editable=False,
                              choices=status.UPLOAD_STATUSES)
    intended_message = models.CharField(max_length=50, null=True)

    status_message = models.CharField(max_length=50, null=True)
    
    
    def __str__(self):
        return self.recipient_name
    
    
    
    
    
    
    