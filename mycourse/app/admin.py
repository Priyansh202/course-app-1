from django.contrib import admin
from .models import *
admin.site.register(Course)

admin.site.register(Lesson)

# Register your models here.

admin.site.register(Enrollment)