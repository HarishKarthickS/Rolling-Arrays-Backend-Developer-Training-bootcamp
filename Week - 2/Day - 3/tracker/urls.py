from django.urls import path
from .views import (
    EmployeeListView, EmployeeCreateView,
    TrainingProgramListView, TrainingProgramCreateView,
    EnrollmentListView
)

urlpatterns = [
    path('employees/', EmployeeListView.as_view(), name='employee_list'),
    path('employees/add/', EmployeeCreateView.as_view(), name='employee_add'),
    # Add URLs for update/delete later if needed
    path('programs/', TrainingProgramListView.as_view(), name='program_list'),
    path('programs/add/', TrainingProgramCreateView.as_view(), name='program_add'),
    # Add URLs for update/delete later if needed
    path('enrollments/', EnrollmentListView.as_view(), name='enrollment_list'),
    # Add URLs for managing enrollments later if needed
] 