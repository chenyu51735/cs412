from django.contrib import admin

# Register your models here.
from .models import Profile

admin.site.register(Profile)

from .models import Item

admin.site.register(Item)

from .models import Transaction

admin.site.register(Transaction)

from .models import Wishlist

admin.site.register(Wishlist)