from django.contrib import admin

# Register your models here.
from .models import CourseDetailes

@admin.register(CourseDetailes)
class CourseDetailesAdmin(admin.ModelAdmin):
    list_display = ['course_name','course_fees','start_time','triner_name','triner_experiecnce']