from django.urls import path
from . import views
from django.contrib import admin


urlpatterns=[
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('admin/', admin.site.urls),
    path('service/',views.service,name='service'),
    path('details/<str:name>/', views.details_view, name='details'),
    path('location/',views.location,name='location'),
    path('about/',views.about,name='about'),

]
