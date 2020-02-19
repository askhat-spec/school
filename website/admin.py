from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post
from .models import Timetable


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    prepopulated_fields = {"slug": ("title",)}


class TimetableAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("grade",)}

admin.site.register(Post, PostAdmin)

admin.site.register(Timetable, TimetableAdmin)