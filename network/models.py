from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(height_field=None, width_field=None, max_length=100, blank=True)
    birth_date = models.DateField(blank=True)


class Subscription(models.Model):
    why_subscribe = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True,
                                      related_name='subscribers')
    to_subscribe = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True,
                                     related_name='to_subscribers')


class Chat(models.Model):
    name = models.CharField(max_length=100)
    profiles = models.ManyToManyField(Profile, on_delete=models.SET_NULL, null=True, related_name='rooms', blank=True)


class Message(models.Model):
    text = models.TextField()
    date = models.DateTimeField(default=datetime.now(), blank=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='messages')
