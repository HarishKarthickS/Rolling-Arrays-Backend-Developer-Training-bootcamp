from django.contrib import admin
from .models import Applicant, InterviewSlot, Assignment

# Register your models here.
admin.site.register(Applicant)
admin.site.register(InterviewSlot)
admin.site.register(Assignment)
