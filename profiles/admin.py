from django.contrib import admin
from . import models
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
	list_display = ['story_title','name','category']



admin.site.register(models.Story, ProfileAdmin)