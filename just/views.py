from django.shortcuts import render, redirect
from util.service import SendMail
# STEP 4 : save data to database
from .models import ContactData
from django.conf import settings


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
    if request.method == 'POST' :
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        message = request.POST.get('message')
        mobile = request.POST.get('mobile')
        profile = request.FILES['profile']

        res = SendMail(fullname, email, 'New Contact Form Submission', message, ['ansariabdulahad3@gmail.com'])
        if res['success'] :
            contact = ContactData(
                fullname = fullname,
                email = email,
                message = message,
                mobile = mobile,
                profile = profile
            )
            contact.save()
            return redirect('/contact')
        else :
            return render(request, 'failed.html')
    data = ContactData.objects.all().values()
    return render(request, 'contact.html', {'data' : data, 'settings' : settings})