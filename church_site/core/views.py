from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'core/base.html')

def donate(request):
    return HttpResponse('donate coming soon...')