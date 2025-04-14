from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView # Using generic views for simplicity
from django.contrib import messages
from .models import Employee, TrainingProgram, Enrollment
from .forms import EmployeeForm, TrainingProgramForm

# Create your views here.

# Employee Views
class EmployeeListView(ListView):
    model = Employee
    template_name = 'tracker/employee_list.html'
    context_object_name = 'employees'

class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'tracker/employee_form.html'
    success_url = reverse_lazy('employee_list') # Redirect to list view after successful creation

    def form_valid(self, form):
        messages.success(self.request, "Employee added successfully!")
        return super().form_valid(form)

# Training Program Views
class TrainingProgramListView(ListView):
    model = TrainingProgram
    template_name = 'tracker/program_list.html'
    context_object_name = 'programs'

class TrainingProgramCreateView(CreateView):
    model = TrainingProgram
    form_class = TrainingProgramForm
    template_name = 'tracker/program_form.html'
    success_url = reverse_lazy('program_list')

    def form_valid(self, form):
        messages.success(self.request, "Training Program added successfully!")
        return super().form_valid(form)

# Enrollment Views (List only for now)
class EnrollmentListView(ListView):
    model = Enrollment
    template_name = 'tracker/enrollment_list.html'
    context_object_name = 'enrollments'
    # Optional: Add ordering or filtering here later
    # queryset = Enrollment.objects.select_related('employee', 'training_program').order_by('employee__name')
