from django.db import models
from django.urls import reverse
# to replace space's in url with -
from django.utils.text import slugify
# for link embeding
import misaka
# getting the current active user
from django.contrib.auth import get_user_model
# user object
User = get_user_model()

# using custom template tags
from django import template
register = template.Library()


# Create your models here.

# A  model for Group
class Group(models.Model):
    # name of the group which is unique
    name = models.CharField(max_length=255,unique=True)
    # slug for generating a valid URL (<title> The 46 Year Old Virgin </title> turn in to <slug> the-46-year-old-virgin </slug>)
    slug = models.SlugField(allow_unicode=True,unique=True)
    # description for the group
    description = models.TextField(blank=True,default='')
    # ??????????????
    description_html = models.TextField(editable=False,default='',blank=True)
    # connecting to users
    members = models.ManyToManyField(User,through="GroupMember")

    # string representation of the group
    def __str__(self):
        return self.name
     
    # saving the group
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args,**kwargs)
    
    # reverse ?????
    def get_absolute_url(self):
        return reverse('groups:single',kwargs={'slug':self.slug})        
    class Meta:
        ordering = ['name']


# A model for GroupMembers
class GroupMember(models.Model):
    # conecting to the group Model
    group = models.ForeignKey(Group,on_delete=models.CASCADE,related_name='memberships')
    # connecting to the user Model
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_groups')

    # a string representation of GroupMember 
    def __str__(self):
        return self.user.username
    # ???????????????????   
    class Meta:
        unique_together = ('group','user')       







