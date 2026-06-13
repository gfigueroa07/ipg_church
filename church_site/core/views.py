from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def messages(request):
    return HttpResponse('messages coming soon...')

def ministries(request):
    return HttpResponse('sermons coming soon...')

def donate(request):
    return HttpResponse('donate coming soon...')

def request_prayer(request):
    return HttpResponse('prayer request coming soon...')

def sermons(request):
    return HttpResponse('sermons coming soon...')