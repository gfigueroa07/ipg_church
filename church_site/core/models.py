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
    
class GalleryImage(models.Model):
    title = models.CharField(
        max_length=100,
        blank=True
    )
    image = models.ImageField(
        upload_to='gallery/'
    )
    is_featured = models.BooleanField(
        default=False
    )
    display_order = models.PositiveIntegerField(
        default=0
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    class Meta:
        ordering = ['display_order']
        
    def save(self, *args, **kwargs):
        if self.is_featured:
            GalleryImage.objects.filter(
                is_featured=True
            ).update(
                is_featured=False
            )
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title or f"Image {self.pk}"