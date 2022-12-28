from django.db import models

# Create your models here.
class Team(models.Model):
    First_name = models.CharField(max_length=255)
    Last_name = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Phone = models.CharField(max_length=255)
    Designation = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.First_name
