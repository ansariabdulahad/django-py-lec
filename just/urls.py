from django.urls import path
# from django.http import HttpResponse
from django.shortcuts import render

def Home(request) :
    return render(
        request,
        'index.html',
        {'name': 'Ahad', 'roll' : '01'}
    )

def About(request) :
    # return HttpResponse("Welcome to About page !")
    return render(
        request,
        'about.html',
        {'menus' : ['Home', 'About', 'Contact', 'Blog']}
    )

def Contact(request) :
    # return HttpResponse("Welcome to Contact page !")
    return render(request, 'contact.html')

urlpatterns = [
    path('', Home),
    path('about', About),
    path('contact', Contact)
]