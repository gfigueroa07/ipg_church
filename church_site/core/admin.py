from django.contrib import admin
from .models import ContactMessage, GalleryImage
# Register your models here.

admin.site.register(ContactMessage)

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display  = (
        'title',
        'is_featured',
        'display_order'
    )
    list_display = (
        'is_featured',
        'display_order'
    )