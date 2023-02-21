from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
# Create your models here.
class Med(models.Model):

    brand_choice = (
        ('GE Healthcare', 'GE Healthcare'),
        ('Samsung', 'Samsung'),
        ('Hitachi', 'Hitachi'),
        ('Philips', 'Philips'),
        ('Siemens', 'Siemens'),
        ('Toshiba', 'Toshiba'),
        ('Aloka', 'Aloka'),
    )

    brand = models.CharField(choices=brand_choice, max_length=255)
    model = models.CharField(max_length=255)
    problem = models.CharField(max_length=1000)
    reason = models.CharField(max_length=1000)
    fixproblem = RichTextField()
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.model
