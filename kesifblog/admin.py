from django.contrib import admin
from .models import Blog_Content,FooterInfo

@admin.register(FooterInfo)
class FooterInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'note')

admin.site.register(Blog_Content)


