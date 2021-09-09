from django.contrib import admin

# Register your models here.
from .models import CourseDetailes,Contact

@admin.register(CourseDetailes)
class CourseDetailesAdmin(admin.ModelAdmin):
    list_display = ['course_name','course_fees','start_time','triner_name','triner_experiecnce']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','mobile_number','enquiry_data']