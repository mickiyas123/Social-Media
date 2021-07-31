from django.conf.urls import url
from django.urls import path

from . import views

# for dynamical url
app_name = 'posts'

urlpatterns = [
    # url to see list of the post
    path('',views.PostList.as_view(),name='all'),
    # path for creating a new post
    path('new/',views.CreatePost.as_view(),name='create'),
    # list of user post
    url('by/(?P<username>[-\w]+)/$',views.UserPosts.as_view(),name='for_user'),
    # pat to single post
    url('by/(?P<username>[-\w]+)/(?P<pk>\d+)/$',views.PostDetail.as_view(),name='single'),
    # path for deleting a post
    url('delete/(?P<pk>\d+)/$',views.DeletePost.as_view(),name='delete')

]

