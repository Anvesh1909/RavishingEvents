from django.urls import path
from . import views
from django.contrib import admin


urlpatterns=[
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('admin/', admin.site.urls),

    path('service/', views.service, name='service'),
    path('details/<str:name>/', views.details_view, name='details'),
    path('location/',views.location,name='location'),
    path('about/',views.about,name='about'),

    path('signup',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout',views.LogoutPage,name='logout'),

]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
