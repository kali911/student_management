from django.contrib import admin
from management.models import Student, Classroom, Major, Course, CourseScore


admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Classroom)
admin.site.register(Major)
admin.site.register(CourseScore)

