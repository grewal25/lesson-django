from django.contrib import admin
from homepage.models import Wall

@admin.register(Wall)
class WallAdmin(admin.ModelAdmin):
    list_display = ('title','slug','publisher')
    prepopulated_fields = {'slug': ('title',)}
    


