from django.contrib import admin
from .models import Department, Level, Student, Subject

# Register your models here.
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Level)
admin.site.register(Subject)