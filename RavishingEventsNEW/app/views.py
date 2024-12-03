from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Service, ServiceImage


# Home Page
def index(request):
    # Use session to maintain visit status
    display_status = not request.session.get('visited', False)
    request.session['visited'] = True

    services = Service.objects.all()

    context = {
        "display": display_status,
        'user': request.user,
        'services': services
    }
    return render(request, 'index.html', context)


# Services Page
def service(request):
    services = Service.objects.all()
    context = {'services': services}
    return render(request, 'service.html', context)


# Service Details Page
def details_view(request, name):
    service = get_object_or_404(Service, name=name)
    images = ServiceImage.objects.filter(service=service)

    context = {
        "service_name": service.name,
        "description": service.description,
        "images": images,
    }
    return render(request, 'details.html', context)


from django.shortcuts import render
from .models import Image

def image_gallery(request):
    images = Image.objects.all()
    return render(request, 'details.html', {'images': images})



# Location Page
def location(request):
    return render(request, 'location.html')


# About Page
def about(request):
    return render(request, 'about.html')


# Signup Page
def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            context = {'error': "Passwords do not match!"}
            return render(request, 'signup.html', context)

        if User.objects.filter(username=uname).exists():
            context = {'error': "Username already taken!"}
            return render(request, 'signup.html', context)

        if User.objects.filter(email=email).exists():
            context = {'error': "Email already registered!"}
            return render(request, 'signup.html', context)

        User.objects.create_user(username=uname, email=email, password=pass1)
        return redirect('login')

    return render(request, 'signup.html')


# Login Page
def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            context = {'error': "Invalid username or password."}
            return render(request, 'login.html', context)

    return render(request, 'login.html')


# Logout
def LogoutPage(request):
    logout(request)
    return redirect('login')
