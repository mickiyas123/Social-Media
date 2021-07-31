# GROUPS URL FILE
# importing the necessary modules
from django.conf.urls import url
from django.urls import path,include
from groups import views

# app name for dynamic url
app_name = 'groups'

urlpatterns = [
    # path for accessing list of the group
    path('',views.ListGroups.as_view(),name='all'),
    # path for creating new group
    path('new/',views.CreateGroup.as_view(),name='create'),
    # path for single group detail
    url(r'posts/in/(?P<slug>[-\w]+)/$',views.SingleGroup.as_view(),name="single"),
    # path for joining a group
    url(r'join/(?P<slug>[-\w]+)/$',views.joinGroup.as_view(),name='join'),
    # path for leaving a group
    url(r'leave/(?P<slug>[-\w]+)/$',views.LeaveGroup.as_view(),name='leave')
    
    
]

