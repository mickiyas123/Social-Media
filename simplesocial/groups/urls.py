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
    path('new/',views.CreateGroup.as_view(),name='Group'),
    # path for single group detail
    url(r'posts/in/(?P<slug>[-\w]+)/',views.SingleGroup.as_view(),name="single")
    
]

