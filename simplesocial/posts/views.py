from django.shortcuts import render
# importing mixins to check login
from django.contrib.auth.mixins import LoginRequiredMixin
# redirecting to html pages
from django.urls import reverse_lazy
# imprting views and HttpResponse
from django.http import Http404
from django.views import generic
# third library mixin
from braces.views import SelectRelatedMixin 
# importing models and forms
from . import models
from . import forms
# importing user model
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.

# posts that belong to the a group
class PostList(SelectRelatedMixin,generic.ListView):
    # connecting to post model
    model = models.Post
    # foreign key for the post
    select_related = ('user','group')
