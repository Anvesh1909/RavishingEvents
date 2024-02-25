from django.shortcuts import render


from django.http import HttpResponse
from django.shortcuts import render,HttpResponse,redirect,reverse
import os

count=0

def index(request):
    global count
    
    context={
        "display" : "True"
    }

    if count==0:
        pass
    else :
        context["display"] = "False"
    count+=1
    
    return render(request, 'index.html', context)


def service(request):
    return render(request, 'service.html')


def details_view(request, name):
    image_folder = 'static/'+name  # Replace with the path to your image folder
    images = [f for f in os.listdir(image_folder) if f.endswith(('jpg', 'jpeg', 'png', 'gif'))]
    print(images)

    service = {
    'Birthday': {
        
        'image': 'birthday.jpg',
                },
    'Wedding': {
        
        'image': 'wedding.jpg',
                },
    'Dj': {
        
        'image': 'DJ.jpg',
                },
    
    'Catering' : {
        
        'image': 'Catering.jpg',
              },
    
    'Haldi' : {
        
        'image': 'haldi.jpg',
        
               },
    'Babyshower' : {
        'disc' : "",
        'image': 'babyshower.jpg', 
                    },
    'Festive' : {
        'disc' : "hello Festive",
        'image': 'Festive.jpg', 
                    },
    'Corporate' : {
        'disc' : "hello Corporate",
        'image': 'Corporate.jpeg', 
                    },
    }
    context = {
        "service_name": name,
        'discription': service[name],
        'images' : images,
    }
    return render(request, 'details.html', context)

def location(request):
    return render(request, 'location.html')


def about(request):
    return render(request, 'about.html')


