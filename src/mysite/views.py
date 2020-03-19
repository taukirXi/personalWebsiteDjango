from django.shortcuts import render, redirect
from django.contrib import messages
from .models import (
    Contact,
)


# Create your views here.


def home(request):
    context = {}
    return render(request, 'mysite/home.html', context)


def portfolio(request):
    context = {}
    return render(request, 'mysite/portfolio.html', context)


def contact(request):
    # TODO: integrate with database; validation of form page
    context = {}
    if request.method == 'POST':
        objemail = request.POST.get('email')
        objsubject = request.POST.get('subject')
        objmessage = request.POST.get('message')

        c = Contact(email=objemail, subject=objsubject, message=objmessage)
        c.save()

        return render(request, 'mysite/contact.html', context=None)
    else:

        return render(request, 'mysite/contact.html', context)
