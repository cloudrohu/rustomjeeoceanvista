from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Avg, Count, Q, F
from django.db.models.functions import Concat
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from django.shortcuts import render



# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import translation

from home.models import *


def index(request):
    header = Setting.objects.all().order_by('-id')[0:1]  
    slider = Web_Slider.objects.all().order_by('-id')[0:6]  
    overview = Overview.objects.all().order_by('-id')[0:1]  
    about_us = About_Us.objects.all().order_by('-id')[0:1]  
    welcome = Welcometo.objects.all().order_by('-id')[0:1]  
    location = Location.objects.all().order_by('-id')[0:1]  
    bookingopen = Bookingopen.objects.all().order_by('-id')[0:1]  
    maharera = Maharera.objects.all().order_by('-id')[0:1]  
    unique_Selling_Proposition = Unique_Selling_Proposition.objects.all() 
    configuration = Configuration.objects.all()
    amenities = Amenities.objects.all()
    views = Gallery.objects.filter(section = 'Views').order_by('-id')
    amenitie = Gallery.objects.filter(section = 'Amenities').order_by('-id')
    interiors = Gallery.objects.filter(section = 'Interiors').order_by('-id')
    exterior = Gallery.objects.filter(section = 'Exterior').order_by('-id')
    plans = Gallery.objects.filter(section = 'Plans').order_by('-id')
    gallery = Gallery.objects.all().order_by('-id')[0:4] 

    context={
        'location':location,
        'maharera':maharera,
        'bookingopen':bookingopen,
        'welcome':welcome,
        'header':header,
        'slider':slider,
        'overview':overview,
        'about_us':about_us,
        'unique_Selling_Proposition':unique_Selling_Proposition,
        'configuration':configuration,
        'amenities':amenities,
        'views':views,
        'amenitie':amenitie,
        'interiors':interiors,
        'exterior':exterior,
        'plans':plans,
        'gallery':gallery,
    }
    return render(request,'index.html',context)
