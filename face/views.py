from django.shortcuts import render
from .models import Cover, Resources, AboutUs

def homePageView(request):
    cover = Cover.objects.all()
    

    context = {
        "cover":cover,
        
    }
    return render(request,'face/home.html' , context)

def newPageView(request):
    resources = Resources.objects.all()
    

    context = {
        "resources":resources,
        
    }
    return render(request,'face/new.html' , context)

def nextPageView (request):
    about_us = AboutUs.objects.all() 


    context = {
        "about_us":about_us
    } 
    return render(request,'face/next.html', context)


