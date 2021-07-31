from django.contrib.auth.signals import user_logged_in
from django.core.checks import messages
from django.db.models import query
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

# list of posts a user created
class UserPosts(generic.ListView):
    # connecting to the model
    model = models.Post
    # connecting to the template
    template_name = 'posts/user_post_list.html'
    
    # checking if user exist and get posts related to that specific user
    def get_queryset(self):
        try:
            # getting the exact posts related to the current loggen in user
            self.post.user = User.objects.prefetch_related('posts').get(username__iexact = self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()    
    # context data object connected to the user
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context 

# a view for displaying post detail
class PostDetail(SelectRelatedMixin,generic.DetailView):
    # connecting to the model
    model = models.Post
    # foreign key
    select_related = ('user','group')
    
    # filtering username
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact = self.kwargs.get('username'))

# Creating Post
class CreatePost(LoginRequiredMixin,SelectRelatedMixin,generic.CreateView):
    fields = ('message','group')
    model = models.Post

    # checking if the form is valid  
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

# Delete Post

class DeletePost(LoginRequiredMixin,SelectRelatedMixin,generic.DeleteView):
    model = models.Post
    select_related = ('user','group')
    success_url = reverse_lazy('posts:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.user.request.user.id)

    def delete(self,*args,**kwargs):
        messages.success(self.request,'Post Deleted')
        return super().delete(*args,**kwargs)    

