from django.contrib import admin
from .models import Employee, TrainingProgram, Enrollment

# Register your models here.
admin.site.register(Employee)
admin.site.register(TrainingProgram)
admin.site.register(Enrollment)
