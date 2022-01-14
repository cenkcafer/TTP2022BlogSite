# A django file which register application in admin site,
# where admin can work on application on backend
from django.contrib import admin
from .models import Blog

# Register your models here.

admin.site.register(Blog)

