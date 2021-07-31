from django.core.checks import messages
from django.db import models
# importing reverse and setting module
from django.urls import reverse
from django.conf import settings

import misaka
# importing Group and User Model
from groups.models import Group
from django.contrib.auth import get_user_model
User  = get_user_model()

# Create your models here.

class Post(models.Model):
    # connecting to the users
    user = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    # created at date
    created_at = models.DateTimeField(auto_now=True)
    # The message of the post
    message = models.TextField()
    # ??????????
    message_html = models.TextField(editable=False)
    # connecting to group
    group = models.ForeignKey(Group,on_delete=models.CASCADE,related_name='groups',null=True,blank=True)

    # a string representation of the method
    def __str__(self):
        return self.message
    # Saving the posts
    def save(self,*args,**kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args,**kwargs)
    # a methd for reversing after posting 
    def get_absolute_url(self):
        return reverse('posts:single',kwargs={'username':self.user.username,'pk':self.pk})
    
    # ??????????
    class Meta:
        ordering = ['-created_at']
        unique_together = ['user','message']    
           
