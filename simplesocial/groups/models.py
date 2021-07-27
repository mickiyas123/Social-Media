from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.db.models.deletion import CASCADE
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
    pass

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

    pass






