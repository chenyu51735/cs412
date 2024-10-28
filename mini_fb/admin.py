from django.contrib import admin

# Register your models here.
from .models import Profile
from .models import StatusMessage
from .models import Image
from .models import Friend
admin.site.register(Profile)
admin.site.register(StatusMessage)
admin.site.register(Image)
admin.site.register(Friend)