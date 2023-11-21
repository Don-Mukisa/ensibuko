from django.contrib import admin

# Register your models here.
from .models import Requisition, UserProfile

admin.site.register(Requisition)
admin.site.register(UserProfile)