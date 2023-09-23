from django.db import models
from datetime import datetime


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    subject = models.CharField(max_length=255)
    messages = models.TextField()
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.email
