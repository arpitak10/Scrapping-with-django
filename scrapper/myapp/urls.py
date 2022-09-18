from django.contrib import admin
from django.urls import path
from . views import *
from myapp import views
#from scrapper.myapp.views import *
#from .models import *
#from scrapper.myapp.views import *
urlpatterns = [
    path('', views.test),
]
