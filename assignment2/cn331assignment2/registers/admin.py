from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Course, Student, Apply, Complete
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ("course_id","course_name","semester","year","current_seat","seat","q_status")

class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id","student_name")

class ApplyAdmin(admin.ModelAdmin):
    list_display = ("course","student")

class CompleteAdmin(admin.ModelAdmin):
    list_display = ("course","student")

admin.site.register(Course,CourseAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Apply,ApplyAdmin)
admin.site.register(Complete,CompleteAdmin)
