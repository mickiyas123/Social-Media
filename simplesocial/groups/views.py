from django.contrib import messages
from django.shortcuts import get_object_or_404, render
# importing permission mixins
from django.contrib.auth.mixins import (LoginRequiredMixin,PermissionRequiredMixin)
# importing reverse for redirecting to different pages
from django.urls import reverse
# importing generic views
from django.views import generic
# importing models of the group webapp
from groups.models import Group,GroupMember
from django.db import IntegrityError
from . import models

# Create your views here.

# class view for creating Posts 
class CreateGroup(LoginRequiredMixin,generic.CreateView):
    # fields we want to edit
    fields = ('name','description')
    # connecting to the model Group
    model = Group

# detail for single group
class SingleGroup(generic.ListView):
    model = Group

# view for List Group
class ListGroups(generic.ListView):
    model = Group 

# view for joining group
class joinGroup(LoginRequiredMixin,generic.RedirectView):

    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})
    def get(self,request,*args,**kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get('slug'))  
        try:
            GroupMember.objects.create(user=self.request.user,group=group)  
        except IntegrityError:
            messages.warning(self.request,"Warning already a member")
        else:
            messages.warning(self.request,"You are now a member")
        return super().get(request,*args,**kwargs)            
# a view for leaving group
class LeaveGroup(LoginRequiredMixin,generic.RedirectView):

    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})
    def get(self,request,*args,**kwargs):
        try:
            membership = GroupMember.objects.filter(user=self.request.user,group__slug=self.kwargs.get('slug')).get()
        except models.GroupMember.DoesNotExist:
            messages.warning(self.request,"Sorry you aren't in this group!")
        else:
            membership.delete()
            messages.success(self.request, "You have left the group")
        return super().get(request,*args,**kwargs)                

