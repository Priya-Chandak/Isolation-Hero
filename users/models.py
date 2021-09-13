from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=16)
    address = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    tax_number = models.CharField(max_length=50)
    date_of_birth = models.DateField(blank=True, null=True)
    permissions = models.CharField(default='', max_length=255)
    
    def __str__(self):
        return self.email

    class Meta(object):
        unique_together = ('email',)
