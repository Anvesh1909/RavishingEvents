from django.db import models

# Model for Services
class Service(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='services/')
    description = models.TextField()

    def __str__(self):
        return self.name


# Model for Service Images (optional, for multiple images per service)
class ServiceImage(models.Model):
    service = models.ForeignKey(Service, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='service_images/')

    def __str__(self):
        return f"Image for {self.service.name}"


from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

