# importing url and path
from django.conf.urls import url
from django.urls import path
# importing django view for login and logout
from django.contrib.auth import logout, views as auth_view
# creating the views we created
from . import views

# app name for 
app_name = 'accounts'

urlpatterns = [
   # a path for login
   path('login',auth_view.LoginView.as_view(template_name = 'accounts/login.htm'),name="login"),
   # a path for logout
   path('logout',auth_view.LogoutView.as_view(),name="logout"),
   # a path for signing up
   path('signup',views.SignUp.as_view(),"signup")
]
