import datetime
from django.core.management.base import BaseCommand
from tracker.models import Employee, TrainingProgram, Enrollment

class Command(BaseCommand):
    help = 'Seeds the database with initial data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')

        # Clear existing data (optional, use with caution)
        # Enrollment.objects.all().delete()
        # Employee.objects.all().delete()
        # TrainingProgram.objects.all().delete()
        # self.stdout.write('Existing data cleared.')

        # Create Employees
        emp1, created_emp1 = Employee.objects.get_or_create(
            email='alice@example.com',
            defaults={'name': 'Alice Wonderland', 'department': 'HR', 'designation': 'Manager'}
        )
        emp2, created_emp2 = Employee.objects.get_or_create(
            email='bob@example.com',
            defaults={'name': 'Bob The Builder', 'department': 'Engineering', 'designation': 'Developer'}
        )
        emp3, created_emp3 = Employee.objects.get_or_create(
            email='charlie@example.com',
            defaults={'name': 'Charlie Chaplin', 'department': 'Marketing', 'designation': 'Analyst'}
        )
        self.stdout.write(f'Created {sum([created_emp1, created_emp2, created_emp3])} Employees.')


        # Create Training Programs
        prog1, created_prog1 = TrainingProgram.objects.get_or_create(
            title='Django Basics',
            defaults={
                'description': 'Introduction to Django framework',
                'start_date': datetime.date.today(),
                'end_date': datetime.date.today() + datetime.timedelta(days=5),
                'trainer_name': 'Jane Doe'
            }
        )
        prog2, created_prog2 = TrainingProgram.objects.get_or_create(
            title='Advanced Python',
             defaults={
                'description': 'Deep dive into Python concepts',
                'start_date': datetime.date.today() + datetime.timedelta(days=10),
                'end_date': datetime.date.today() + datetime.timedelta(days=20),
                'trainer_name': 'John Smith'
            }
        )
        self.stdout.write(f'Created {sum([created_prog1, created_prog2])} Training Programs.')

        # Create Enrollments
        Enrollment.objects.get_or_create(
            employee=emp1,
            training_program=prog1,
            defaults={'status': 'ENROLLED'}
        )
        Enrollment.objects.get_or_create(
            employee=emp2,
            training_program=prog1,
            defaults={'status': 'IN_PROGRESS'}
        )
        Enrollment.objects.get_or_create(
            employee=emp2,
            training_program=prog2,
            defaults={'status': 'ENROLLED'}
        )
        Enrollment.objects.get_or_create(
            employee=emp3,
            training_program=prog2,
            defaults={'status': 'COMPLETED'}
        )
        # Note: Counting created enrollments is slightly more complex with get_or_create if not tracking the 'created' flag for each.
        # For simplicity, we won't print the count here, but assume they are created if they don't exist.
        self.stdout.write('Created Enrollments.')


        self.stdout.write(self.style.SUCCESS('Data seeding completed successfully!')) 