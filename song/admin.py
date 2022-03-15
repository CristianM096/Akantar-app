from django.contrib import admin
from . import models
# Register your models here.
class SongAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    

admin.site.register(models.Song,SongAdmin)
