from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

from common.models import Admin

# Register your models here.
admin.site.unregister(Group)

admin.site.unregister(User)
admin.site.register(Admin, UserAdmin)
