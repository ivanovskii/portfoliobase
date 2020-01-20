from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    location = models.TextField(null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


class Portfolio(models.Model):
    name = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Item(models.Model):
    headline = models.TextField(null=True)
    pic = models.ImageField(blank=True, null = True)
    description = models.TextField(null=True)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)