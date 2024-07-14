# from django.http import HttpResponse
from django.urls import path
from .views import Home, About, Contact
from django.contrib import admin

urlpatterns = [
    path('', Home),
    path('about', About),
    path('contact', Contact),
    path('admin/', admin.site.urls)
]