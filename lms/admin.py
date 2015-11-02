from django.contrib import admin
from .models import Course
from .models import Unit
from .models import Lesson


class UnitInline(admin.StackedInline):
    model = Unit
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                'fields': ['title', 'logo', 'summary']
            }
        ),
        (
            u'Detalhes',
            {
                'fields': ['pub_date', 'description'],
                'classes': ['collapse']
            }
        )
    ]
    inlines = [UnitInline]
    list_display = ('title', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['title']

# Register your models here.
admin.site.register(Course, CourseAdmin)
# admin.site.register(Unit)
admin.site.register(Lesson)
