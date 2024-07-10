from django.shortcuts import render
from util.service import SendMail


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

        res = SendMail('Testing...', message, ['ansariabdulahad3@gmail.com'])
        print(res)
    return render(request, 'contact.html')