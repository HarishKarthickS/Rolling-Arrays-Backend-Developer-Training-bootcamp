from django import forms
from .models import Employee, TrainingProgram, Enrollment

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'department', 'designation']

class TrainingProgramForm(forms.ModelForm):
    class Meta:
        model = TrainingProgram
        fields = ['title', 'description', 'start_date', 'end_date', 'trainer_name']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['employee', 'training_program', 'status'] 