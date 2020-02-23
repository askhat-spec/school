from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post
from .models import Timetable
from .models import Teachers
from .models import Awards

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    prepopulated_fields = {"slug": ("title",)}

class TimetableAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("grade",)}
    

admin.site.register(Post, PostAdmin)
admin.site.register(Timetable, TimetableAdmin)
admin.site.register(Teachers)
admin.site.register(Awards)