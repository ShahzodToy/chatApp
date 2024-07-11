from django.db import models
from django.contrib.auth.models import User
import shortuuid

class ChatGroup(models.Model):
    group_name = models.CharField(max_length=200,unique=True,default=shortuuid.uuid)
    online_users = models.ManyToManyField(User,related_name='online_in_groups',blank=True)
    groupchat_name = models.CharField(max_length=128,null=True,blank=True)
    admin = models.ForeignKey(User,related_name='groupchats',blank=True,null=True,on_delete=models.SET_NULL)
    members = models.ManyToManyField(User,related_name='chat_groups',blank=True)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.group_name

class ChatMessage(models.Model):
    group = models.ForeignKey(ChatGroup,on_delete=models.CASCADE,related_name='chat_message')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.body
