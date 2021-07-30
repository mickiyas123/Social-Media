from django.shortcuts import render
# importing permission mixins
from django.contrib.auth.mixins import (LoginRequiredMixin,PermissionRequiredMixin)
# importing reverse for redirecting to different pages
from django.urls import reverse
# importing generic views
from django.views import generic
# importing models of the group webapp
from groups.models import Group,GroupMember

# Create your views here.

# class view for creating Posts 
# class CreatePost(LoginRequiredMixin,generic.CreateView):
#     fields = ('name','description')
#     model = 

