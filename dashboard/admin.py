from django.contrib import admin
from .models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['uniqueId','user','position_title','call','country','slug','last_updated']
    list_display_links = ['uniqueId','user','position_title']
