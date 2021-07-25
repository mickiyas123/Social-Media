from django.db import models
# importing reverse lazy for redirecting
from django.urls import reverse_lazy
# importing auth 
from django.contrib  import auth

# Create your models here.

# model for users
class Users(auth.models.User):
     
    # a string representation of the object 
    def __str__(self):
        return "@{}".format(self.username)
