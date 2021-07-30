from groups.models import Group
from django.contrib import admin
# importing the models
from . import models

# Register your models here.



# registering the group model
admin.site.register(models.Group)
