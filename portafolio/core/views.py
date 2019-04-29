from django.shortcuts import render, HttpResponse
from core.models import Home, About, Contact, Red

def home(request):
    home_ = Home.objects.get(pk=1)
    red = Red.objects.all()
    return render(request, "core/home.html",{'home':home_,'red':red})
def about(request):
    About_ = About.objects.get(pk=2)
    return render(request, "core/about.html", {'about':About_})

def portfolio(request):
    return render(request, "core/portfolio.html")

def contact(request):
    Contact_ = Contact.objects.get(pk=1)
    return render(request, "core/contact.html", {'contact':Contact_})