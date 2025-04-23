from django.contrib import admin
from .models import Applicant, InterviewSlot, Assignment

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'job_applied_for')
    search_fields = ('name', 'email', 'job_applied_for')
    list_filter = ('job_applied_for',)
    ordering = ('name',)

@admin.register(InterviewSlot)
class InterviewSlotAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'interviewer_name', 'job_role', 'status')
    list_filter = ('status', 'job_role', 'date')
    search_fields = ('interviewer_name', 'job_role')
    ordering = ('date', 'time')
    fieldsets = (
        (None, {'fields': ('date', 'time', 'interviewer_name', 'job_role')}),
        ('Status', {'fields': ('status',)}),
    )

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'interview_slot')
    search_fields = ('applicant__name', 'interview_slot__job_role')
    list_filter = ('interview_slot__job_role', 'interview_slot__status')
    ordering = ('interview_slot',)
