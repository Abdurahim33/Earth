from django.contrib import admin
from About.models import Backround_image, About_model

@admin.register(Backround_image)
class Backround_admin(admin.ModelAdmin):
    list_display = ('image',)
    list_display_links = ('image',)


@admin.register(About_model)
class  About_admin(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'text')
    list_display_links = ('title', 'sub_title', 'text')
    
