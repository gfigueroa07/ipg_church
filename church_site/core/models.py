from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from phonenumber_field.modelfields import PhoneNumberField
from urllib.parse import urlparse, parse_qs
from django.db import models



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
    
class GalleryAlbum(models.Model):
    title = models.CharField(
        max_length=100
    )
    display_order = models.PositiveBigIntegerField(
        default=0
    ) 
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    def __str__(self):
        return self.title
    
class GalleryImage(models.Model):
    album = models.ForeignKey(
        GalleryAlbum,
        on_delete=models.CASCADE,
        related_name='images',
        null=False,
        blank=False,
    )
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
                album=self.album,
                is_featured=True
            ).exclude(pk=self.pk).update(
                is_featured=False
            )
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title or f"Image {self.pk}"
    
class Sermon(models.Model):
    title = models.CharField(
        max_length=200
    )
    youtube_url = models.URLField()
    sermon_date = models.DateField()
    thumbnail = models.ImageField(
        upload_to='sermons/',
        blank=True,
        null=True
    )
    @property
    def embed_url(self):
        parsed = urlparse(self.youtube_url)

        # youtube.com/watch?v=...
        if "youtube.com" in parsed.netloc:
            video_id = parse_qs(parsed.query).get("v", [None])[0]

        # youtu.be/...
        elif "youtu.be" in parsed.netloc:
            video_id = parsed.path.lstrip("/")

        else:
            return ""

        return f"https://www.youtube.com/embed/{video_id}"