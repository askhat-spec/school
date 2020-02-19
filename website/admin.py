from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post
 


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)