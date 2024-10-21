from django.db import models
from django.urls import reverse
# Create your models here.
class Profile(models.Model):

    first_name = models.TextField(blank=False)
    last_name = models.TextField(blank=False)
    city = models.TextField(blank=False)
    email = models.TextField(blank=False)
    image_url = models.URLField(blank=True)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk})

    def get_status_messages(self):
        messages = StatusMessage.objects.filter(profile=self)
        return messages
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class StatusMessage(models.Model):

    timestamp = models.DateTimeField(auto_now=True)
    message = models.TextField(blank=True)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)

    def get_images(self):
        images = Image.objects.filter(status_message=self)
        return images
    
    def __str__(self):
        return f'{self.message}'
    

class Image(models.Model):

    timestamp = models.DateTimeField(auto_now=True)
    image_file = models.ImageField(blank=True)
    status_message = models.ForeignKey("StatusMessage", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.image_file}'