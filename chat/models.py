from datetime import date
from django.db import models
from django.conf import settings

class Contact(models.Model):
    contact = models.CharField(max_length=15)
    male = models.BooleanField(default=True)

class Chat(models.Model):
    created_at = models.DateField(default=date.today)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=None, blank=True, null=True, related_name='author_chat_set')
    receiver = models.ForeignKey(Contact,on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='receiver_chat_set')

class Message(models.Model):
    text = models.CharField(max_length=500)
    created_at = models.DateField(default=date.today)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='chat_message_set')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_message_set')
    receiver = models.ForeignKey(Contact,on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='receiver_message_set')
    

