from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class ContactMessage(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = PhoneNumberField(region="US")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return self.full_name