from django.contrib import admin
from .models import Service, ServiceImage

admin.site.register(Service)
admin.site.register(ServiceImage)


from django.contrib import admin
from .models import Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description')
