from django.db import models

# Create your models here.
class Profile(models.Model):

    first_name = models.TextField(blank=False)
    last_name = models.TextField(blank=False)
    city = models.TextField(blank=False)
    email = models.TextField(blank=False)
    image_url = models.URLField(blank=True)


    def _str_(self):
        return f'{self.last_name} by {self.email}'