from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):

    first_name = models.TextField(blank=False)
    last_name = models.TextField(blank=False)
    city = models.TextField(blank=False)
    email = models.TextField(blank=False)
    image_url = models.URLField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk})

    def get_status_messages(self):
        messages = StatusMessage.objects.filter(profile=self)
        return messages
    
    def get_friends(self):
        friend1 = Friend.objects.filter(profile1=self)
        friend2 = Friend.objects.filter(profile2=self)
        friends_profiles = [friend.profile2 for friend in friend1] + \
                           [friend.profile1 for friend in friend2]

        return friends_profiles
    
    def add_friend(self, other):
        if self == other:
            raise "You cannot be friends with yourself."
        friendship_exists = Friend.objects.filter(
            models.Q(profile1=self, profile2=other) | 
            models.Q(profile1=other, profile2=self)
        ).exists()

        if not friendship_exists:
            Friend.objects.create(profile1=self, profile2=other)

    def get_friend_suggestions(self):
        friends = self.get_friends()
        friend_ids = [friend.pk for friend in friends]
        suggestions = Profile.objects.exclude(pk=self.pk).exclude(pk__in=friend_ids)
        return suggestions

    def get_news_feed(self):
        friends = self.get_friends()
        profile_ids = [friend.pk for friend in friends]
        news_feed = StatusMessage.objects.filter(profile__id__in=profile_ids).order_by('-timestamp')
        return news_feed
    
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
    

class Friend(models.Model):

    profile1 = models.ForeignKey("Profile", related_name="profile1", on_delete=models.CASCADE)
    profile2 = models.ForeignKey("Profile", related_name="profile2", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.profile1.first_name} {self.profile1.last_name} & {self.profile2.first_name} {self.profile2.last_name}'