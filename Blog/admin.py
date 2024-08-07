from django.contrib import admin
from .models import *

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display=('author','created_on',)
admin .site.register(Blog,BlogAdmin) 

admin.site.register(Profile)
admin.site.register(Comment)

admin.site.site_header = 'My Blog Admin'
admin.site.site_title = 'My Blog Admin Portal'
admin.site.index_title = 'Welcome to My Blog Admin'

