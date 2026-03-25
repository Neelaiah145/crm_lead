from django.contrib import admin

# Register your models here.
from leads.models import User

admin.site.register(User)