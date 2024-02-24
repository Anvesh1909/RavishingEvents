from django.shortcuts import render


from django.http import HttpResponse
from django.shortcuts import render,HttpResponse,redirect,reverse
import os

# from .models import FormData

# count=0
# context={
#         "form" : count,
#         "user" : 0
#     }



def index(request):
    # global count,context
    
    
    # if request.method == 'POST':
        
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     phone = request.POST.get('phone')
    #     count+=1
        
    #     form_data = FormData(name=name, email=email, phone=phone)
    #     form_data.save()
        
    #     context={
    #         "form" : count,
    #         "user": {
    #             "name": name,
    #             "email": email,
    #             "phone": phone
    #         }
    #     }
        
    #     print(context,name,email,phone)
        
    #     return redirect(request.path, kwargs=context) # Redirect to a success page after saving data
    
  
    return render(request, 'index.html')


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
        
        'image': 'dj.jpg',
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


