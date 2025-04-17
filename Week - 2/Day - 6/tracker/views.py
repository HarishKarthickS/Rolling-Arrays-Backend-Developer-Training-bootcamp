from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib import messages
from django.db.models import Count
from .models import Employee, TrainingProgram, Enrollment
from .forms import EmployeeForm, TrainingProgramForm, EnrollmentForm

# Create your views here.

# Dashboard View
class DashboardView(TemplateView):
    template_name = 'tracker/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get total counts
        context['total_employees'] = Employee.objects.count()
        context['total_programs'] = TrainingProgram.objects.count()
        context['total_enrollments'] = Enrollment.objects.count()
        
        # Get status distribution
        status_counts = Enrollment.objects.values('status').annotate(count=Count('status'))
        context['status_counts'] = {item['status']: item['count'] for item in status_counts}
        
        # Get department distribution
        dept_counts = Employee.objects.values('department').annotate(count=Count('department'))
        context['department_counts'] = {item['department']: item['count'] for item in dept_counts}
        
        # Get recent enrollments
        context['recent_enrollments'] = Enrollment.objects.select_related('employee', 'training_program').order_by('-id')[:5]
        
        # Add status choices for the chart
        context['status_choices'] = Enrollment.STATUS_CHOICES
        
        return context

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

# Enrollment Views
class EnrollmentListView(ListView):
    model = Enrollment
    template_name = 'tracker/enrollment_list.html'
    context_object_name = 'enrollments'
    
    def get_queryset(self):
        queryset = Enrollment.objects.select_related('employee', 'training_program')
        
        # Filter by status if provided
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)
            
        # Filter by department if provided
        department = self.request.GET.get('department')
        if department:
            queryset = queryset.filter(employee__department=department)
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add status choices for the filter
        context['status_choices'] = Enrollment.STATUS_CHOICES
        # Get unique departments for filtering
        context['departments'] = Employee.objects.values_list('department', flat=True).distinct()
        # Add current filters to context
        context['current_status'] = self.request.GET.get('status', '')
        context['current_department'] = self.request.GET.get('department', '')
        return context

class EnrollmentCreateView(CreateView):
    model = Enrollment
    form_class = EnrollmentForm
    template_name = 'tracker/enrollment_form.html'
    success_url = reverse_lazy('enrollment_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Enrollment added successfully!')
        return super().form_valid(form)
