from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class TrainingProgram(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    trainer_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title

class Enrollment(models.Model):
    STATUS_CHOICES = [
        ('ENROLLED', 'Enrolled'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='enrollments')
    training_program = models.ForeignKey(TrainingProgram, on_delete=models.CASCADE, related_name='enrollments')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ENROLLED')

    def __str__(self) -> str:
        employee_name = self.employee.name if self.employee else "Unknown Employee"
        program_title = self.training_program.title if self.training_program else "Unknown Program"
        return f"{employee_name} - {program_title} ({self.get_status_display()})"
