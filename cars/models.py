from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db.models.signals import post_save
from django.conf import settings
# Create your models here.


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    

def create_user_profile(sender, instance, created, *args, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=settings.AUTH_USER_MODEL)

class Winners(models.Model):
    user = models.CharField(max_length=50)

    def __str__(self):
        return self.user


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=254, blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return self.name

