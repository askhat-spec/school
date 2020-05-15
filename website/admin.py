from django.contrib import admin
from django.utils.safestring import mark_safe
from django_summernote.admin import SummernoteModelAdmin
from .models import Post
from .models import Timetable
from .models import Teachers
from .models import Awards
from django.contrib.auth.models import User, Group


admin.site.unregister(User)
admin.site.unregister(Group)

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    prepopulated_fields = {"slug": ("title",)}

class TimetableAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("grade",)}
    

admin.site.register(Post, PostAdmin)
admin.site.register(Timetable, TimetableAdmin)

@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    # Учителя
    list_display = ("name", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src = {obj.cover.url} width = "80" height = "auto"')

    get_image.short_description = "Фото"


@admin.register(Awards)
class AwardsAdmin(admin.ModelAdmin):
    # Награды
    list_display = ("name", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src = {obj.cover.url} width = "80" height = "auto"')

    get_image.short_description = "Фото"


admin.site.site_title = "Школа 56"
admin.site.site_header = "Школа 56"