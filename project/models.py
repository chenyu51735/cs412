from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
from django.core.validators import MinValueValidator, MaxValueValidator
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
    image_file = models.ImageField(blank=False)
    rating = models.DecimalField(decimal_places=2, max_digits=3, default=5.00)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='project_profile')

    def get_absolute_url(self):
        return reverse('project_profile', kwargs={'pk': self.pk})
    
    def get_items(self):
        return Item.objects.filter(seller=self)

    def update_rating(self):
        """
        Updates the average rating based on all related transactions.
        """
        from .models import Transaction
        seller_ratings = list(Transaction.objects.filter(item__seller=self).exclude(seller_rating__isnull=True).values_list('seller_rating', flat=True))
        buyer_ratings = list(Transaction.objects.filter(buyer=self).exclude(buyer_rating__isnull=True).values_list('buyer_rating', flat=True))
        all_ratings = seller_ratings + buyer_ratings

        if all_ratings:
            self.rating = sum(all_ratings) / len(all_ratings)
        else:
            self.rating = 5.00
        self.save()

    def get_wishlist(self):
        """
        Retrieve all items in the user's wishlist.
        """
        return Wishlist.objects.filter(profile=self)
    
    def add_transaction(self, item, buyer):
        """
        Add a transaction for the profile.
        """
        if self==item.seller:
            raise "You cannot be buy your own item."
        transaction = Transaction.objects.create(item=item, buyer=buyer)
        return transaction

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Item(models.Model):
    '''
    Represent each item listed for sale
    '''
    class Category(models.TextChoices):
        ELECTRONICS = 'Electronics', 'Electronics'
        HOME = 'Home', 'Home'
        COLLECTIBLES = 'Collectibles', 'Collectibles'
        CLOTHING = 'Clothing, Shoes & Accessories', 'Clothing, Shoes & Accessories'
        SPORTING_GOODS = 'Sporting Goods', 'Sporting Goods'
        JEWELRY = 'Jewelry & Watches', 'Jewelry & Watches'
        BUSINESS = 'Business & Industrial', 'Business & Industrial'

    class Condition(models.TextChoices):
        NEW = 'New', 'New'
        LIKE_NEW = 'Like New', 'Like New'
        GOOD = 'Good', 'Good'
        ACCEPTABLE = 'Acceptable', 'Acceptable'
        POOR = 'Poor', 'Poor'

    title = models.TextField(blank=False)
    product = models.TextField(blank=False)
    description = models.TextField(blank=True)
    brand = models.TextField(blank=False)
    category = models.CharField(max_length=50, choices=Category.choices, blank=False, default=Category.ELECTRONICS)
    condition = models.CharField(max_length=50, choices=Condition.choices, blank=False, default=Condition.NEW)
    price = models.DecimalField(decimal_places=2, max_digits=11)
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='item_seller')
    images = models.ImageField(blank=False)
    post_date = models.DateTimeField(auto_now=True)
    sold = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.product}'

class Transaction(models.Model):
    '''
    Represent completed purchases or sales of items.
    '''
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='buyer')
    transaction_date = models.DateTimeField(auto_now=True)
    seller_rating = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    buyer_rating = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    ) 
    def __str__(self):
        return f'{self.item.seller} sold {self.item} to {self.buyer} at {self.transaction_date}'
    
class Wishlist(models.Model):
    '''
    Save items to wishlist for future viewing
    '''
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='wishlist_profile')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='wishlist_item')
    added_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.profile.first_name} {self.profile.last_name} added {self.item} to wishlist'