from django.contrib.auth import get_user_model
from django.db import models

from django.contrib.auth.models import AbstractUser

User = get_user_model()

class Section(models.Model):
    title = models.CharField(max_length=50);
    image = models.ImageField(upload_to='images/sections')

    def __str__(self):
        return f'{self.id}: {self.title}'

class Conversation(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='conversations')
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} : {self.text} | {self.created_at}'

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        auther = self.user.get_full_name() or self.user.username
        return f'{auther} : {self.text} | {self.created_at}'

#print(Section.objects.all().count())