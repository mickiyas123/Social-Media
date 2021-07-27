from django.db import models
# to replace space's in url with -
from django.utils.text import slugify
# for link embeding
import misaka
# getting the current active user
from django.contrib.auth import get_user_model
# user object
User = get_user_model()

# using custom template tags
from django import template
register = template.Library()




