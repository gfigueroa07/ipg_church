from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from core.models import ContactMessage, GalleryImage, GalleryAlbum, Sermon
from church_site.forms import ContactForm
from django.contrib import messages


# Create your views here.

def home(request):
    form = ContactForm(request.POST or None)
    featured = GalleryImage.objects.filter(
        is_featured=True
    ).first()
    gallery_items = GalleryImage.objects.exclude(
        is_featured=True
    )[:6]
    context = {
        'featured': featured,
        'gallery_items': gallery_items
    }
    if request.method == "POST":
        if form.is_valid():
            contact = form.save()
            send_mail(
            subject=f"Contact - {form.cleaned_data['full_name']}",
            message=form.cleaned_data["message"],
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CONTACT_EMAIL],
            )
            messages.success(
                request, 
                "Thank you for contacting us. Your message has been received and we will respond within 24 hours."
            )
            
            return redirect("/#contact")
        else:
            messages.error(
                request,
                'Please correct the errors below and try again.'
            )
    return render(request, 'core/home.html', {
        'form': form,
        'featured': featured,
        'gallery_items': gallery_items
    })

def about(request):
    return render(request, 'core/about.html')

def ministries(request):
    return render(request, 'core/ministries.html')

def sermons(request):
    sermons = Sermon.objects.order_by(
        '-sermon_date'
    )[:3]
    # recent_sermons = Sermon.objects.order_by('-sermon_date')[:3]
    return render(request, 'core/sermons.html',  {
        'sermons': sermons
    })

def gallery(request):
    albums = GalleryAlbum.objects.prefetch_related(
        'images'
    ).order_by('display_order')
    return render(request, 'core/gallery.html', {
        'albums': albums
    })