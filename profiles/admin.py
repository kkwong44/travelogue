'''
Administration to Django Control Panel
'''
from django.contrib import admin
from .models import Users

# Register User Profile
admin.site.register(Users)
