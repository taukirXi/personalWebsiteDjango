from django.shortcuts import render


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
    return render(request, 'mysite/contact.html', context)
