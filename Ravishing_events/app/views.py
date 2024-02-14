from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse,redirect,reverse

from .models import FormData

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
    service = {
    'Birthday': {
        'disc' : "hello birthday",
        'image': 'birthday.jpg',
                },
    'Wedding': {
        'disc' : "hello wedding",
        'image': 'wedding.jpg',
                },
    'Dj': {
        'disc' : "hello dj",
        'image': 'dj.jpg',
                },
    
    'Holi' : {
        'disc' : "hello holi",
        'image': 'holi.jpg',
              },
    
    'Huldi' : {
        'disc' : "hello huldi",
        'image': 'huldi.jpg',
               },
    'Babyshower' : {
        'disc' : "hello babyshower",
        'image': 'babyshower.jpeg', 
                    },
    'Festive' : {
        'disc' : "hello Festive",
        'image': 'Festive.jpeg', 
                    },
    }
    context = {
        "service_name": name,
        'discription': service[name],
    }
    return render(request, 'details.html', context)

def location(request):
    return render(request, 'location.html')


def about(request):
    return render(request, 'about.html')


