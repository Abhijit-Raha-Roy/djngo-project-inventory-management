from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Laptop,Desktop,Mobile)
class ViewAdmin(admin.ModelAdmin):
    pass