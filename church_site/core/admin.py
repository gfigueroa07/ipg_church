from django.contrib import admin
from .models import ContactMessage, GalleryImage, GalleryAlbum, Sermon
# Register your models here.

admin.site.register(ContactMessage)

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'album',
        'is_featured',
        'display_order',
    )
    
@admin.register(GalleryAlbum)
class GalleryAlbumAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'display_order',
        'created_at',
    )
    
@admin.register(Sermon)
class SermonAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'youtube_url',
        'sermon_date',
    )