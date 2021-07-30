from groups.models import Group, GroupMember
from django.contrib import admin
# importing the models
from . import models

# Register your models here.

# i can see the group members when i click the group an i can edit the group members
class GroupMemberInline(admin.TabularInline):
    model = GroupMember


# registering the group model
admin.site.register(models.Group)
