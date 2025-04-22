from django.shortcuts import render, redirect
from .models import Applicant, InterviewSlot, Assignment
from django.db import IntegrityError

# Home view
def home(request):
    return render(request, 'interviews/home.html')

# List all applicants
def applicant_list(request):
    applicants = Applicant.objects.all()
    return render(request, 'interviews/applicant_list.html', {'applicants': applicants})

# List all interview slots
def slot_list(request):
    slots = InterviewSlot.objects.all()
    return render(request, 'interviews/slot_list.html', {'slots': slots})

# Update interview slot status
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.urls import reverse

def update_slot_status(request, slot_id):
    slot = InterviewSlot.objects.get(id=slot_id)
    valid_transitions = {
        'Scheduled': ['Completed', 'Cancelled'],
        'Available': ['Scheduled', 'Cancelled'],
        'Completed': [],
        'Cancelled': [],
    }
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in valid_transitions.get(slot.status, []):
            slot.status = new_status
            slot.save()
        return HttpResponseRedirect(reverse('slot_list'))
    return render(request, 'interviews/update_slot_status.html', {
        'slot': slot,
        'valid_statuses': valid_transitions.get(slot.status, []),
    })

# List all assignments
def assignment_list(request):
    assignments = Assignment.objects.select_related('applicant', 'interview_slot').all()
    return render(request, 'interviews/assignment_list.html', {'assignments': assignments})

# Assign an applicant to an interview slot (1-to-1 mapping)
def assign_interview(request):
    error = None
    if request.method == 'POST':
        applicant_id = request.POST.get('applicant')
        slot_id = request.POST.get('slot')
        try:
            applicant = Applicant.objects.get(id=applicant_id)
            slot = InterviewSlot.objects.get(id=slot_id)
            if slot.status != 'Available':
                error = 'Slot is not available.'
            elif Assignment.objects.filter(applicant=applicant).exists():
                error = 'Applicant already assigned to a slot.'
            else:
                Assignment.objects.create(applicant=applicant, interview_slot=slot)
                slot.status = 'Scheduled'
                slot.save()
                return redirect('assignment_list')
        except (Applicant.DoesNotExist, InterviewSlot.DoesNotExist):
            error = 'Invalid applicant or slot.'
        except IntegrityError:
            error = 'This slot is already assigned.'
    applicants = Applicant.objects.all()
    slots = InterviewSlot.objects.filter(status='Available')
    return render(request, 'interviews/assign_interview.html', {
        'applicants': applicants,
        'slots': slots,
        'error': error
    })
