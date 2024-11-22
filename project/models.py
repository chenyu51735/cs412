from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    '''
    Stores personal information about each user
    '''
    first_name = models.TextField(blank=False)
    last_name = models.TextField(blank=False)
    nick_name = models.TextField(blank=True)
    email = models.TextField(blank=False)
    phone = models.TextField(blank=False)
    city = models.TextField(blank=True)
    bio = models.TextField(blank=True)
    image_file = models.ImageField(blank=True)
    rating = models.DecimalField(decimal_places=2, max_digits=3, default=0.00)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_profile')

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk})
    
    def get_items(self):
        return Item.objects.filter(user=self)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Item(models.Model):
    '''
    Represent each item listed for sale
    '''
    title = models.TextField(blank=False)
    product = models.TextField(blank=False)
    description = models.TextField(blank=True)
    brand = models.TextField(blank=False)
    category = models.TextChoices('Electronics', 'Home', 'Collectibles', 'Clothing, Shoes & Accessories',
                                  'Sporting Goods', 'Jewelry & Watches', 'Business & Industrial')
    Condition = models.TextChoices('New', 'Like New', 'Good', 'acceptable', 'poor')
    price = models.DecimalField(decimal_places=2, max_digits=11)
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='item_seller')
    images = models.ImageField(blank=False)
    post_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.product}'

class Transaction(models.Model):
    '''
    Represent completed purchases or sales of items.
    '''
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='buyer')
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='seller')
    transaction_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<<{self.item}>> {self.transaction_date}'
    
class Wishlist(models.Model):
    '''
    Save items to wishlist for future viewing
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='wishlist_item')
    added_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.item} {self.user}'
