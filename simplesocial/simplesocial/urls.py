"""simplesocial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# importing views we created
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # a path for accessing home page view
    path('',views.HomePage.as_view(),name='home'),
    # a path for connecting the project and webapp
    path('accounts',include('accounts.urls',namespace="accounts")),
    # a path for authorization purpose
    path('accounts',include('django.contrib.auth.urls')),
    # a path for test view
    path('test',views.Test.as_view(),name ='test'),
    # a path for thankyou view
    path('thankyou',views.ThankYou.as_view(),name='thanks')

]
