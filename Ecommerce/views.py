from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.conf import settings
import json
import os
def home(request):
    title = {
        'title': 'Home',
    }
    return render(request,'index.html',context=title)
def contact(request):
    title = {
        'title': 'Contact',
    }
    return render(request,'contact.html',context=title)
