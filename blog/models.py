from django.db import models

# Create your models here.

class Article(models.Model):

    title = models.TextField(blank=False)
    auther = models.TextField(blank=False)
    text = models.TextField(blank=False)
    published = models.DateTimeField(auto_now = True)
    image_url = models.URLField(blank=True)


    def _str_(self):
        return f'{self.title} by {self.author}'
        