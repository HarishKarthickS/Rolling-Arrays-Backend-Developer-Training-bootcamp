from django.core.management.base import BaseCommand
from interviews.models import Applicant, InterviewSlot, Assignment
from django.utils import timezone
import random

class Command(BaseCommand):
    help = 'Seed the database with dummy applicants, slots, and assignments.'

    def handle(self, *args, **kwargs):
        Applicant.objects.all().delete()
        InterviewSlot.objects.all().delete()
        Assignment.objects.all().delete()

        # Applicants
        applicants = [
            Applicant(name='Alice Johnson', email='alice@example.com', job_applied_for='Frontend Developer'),
            Applicant(name='Bob Smith', email='bob@example.com', job_applied_for='Backend Developer'),
            Applicant(name='Carol Lee', email='carol@example.com', job_applied_for='Data Scientist'),
            Applicant(name='David Kim', email='david@example.com', job_applied_for='DevOps Engineer'),
        ]
        Applicant.objects.bulk_create(applicants)

        # Interview Slots
        today = timezone.now().date()
        slots = [
            InterviewSlot(date=today, time='09:00', interviewer_name='Eve HR', job_role='Frontend Developer', status='Available'),
            InterviewSlot(date=today, time='10:00', interviewer_name='Frank HR', job_role='Backend Developer', status='Scheduled'),
            InterviewSlot(date=today, time='11:00', interviewer_name='Grace HR', job_role='Data Scientist', status='Completed'),
            InterviewSlot(date=today, time='12:00', interviewer_name='Heidi HR', job_role='DevOps Engineer', status='Cancelled'),
        ]
        InterviewSlot.objects.bulk_create(slots)

        # Assignments (link Bob Smith to Backend Developer slot)
        slot = InterviewSlot.objects.get(job_role='Backend Developer')
        applicant = Applicant.objects.get(name='Bob Smith')
        Assignment.objects.create(interview_slot=slot, applicant=applicant)

        self.stdout.write(self.style.SUCCESS('Dummy data seeded successfully.'))
