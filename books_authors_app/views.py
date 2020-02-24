from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        'all_dojo': Dojo.objects.all()
    }
    return render(request, 'index.html')