from django.contrib import admin

# Register your models here.
from .models import Profile
from .models import StatusMessage
from .models import Image
admin.site.register(Profile)
admin.site.register(StatusMessage)
admin.site.register(Image)