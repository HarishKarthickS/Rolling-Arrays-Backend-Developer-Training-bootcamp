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
from django.db.models import Q
from datetime import datetime

def slot_list(request):
    slots = InterviewSlot.objects.all()
    job_role_query = request.GET.get('job_role', '').strip()
    status_query = request.GET.get('status', '').strip()
    date_query = request.GET.get('date', '').strip()

    if job_role_query:
        slots = slots.filter(job_role__icontains=job_role_query)
    if status_query:
        slots = slots.filter(status=status_query)
    if date_query:
        try:
            date_obj = datetime.strptime(date_query, '%Y-%m-%d').date()
            slots = slots.filter(date=date_obj)
        except ValueError:
            pass
    return render(request, 'interviews/slot_list.html', {
        'slots': slots,
        'job_role_query': job_role_query,
        'status_query': status_query,
        'date_query': date_query,
    })

# Create a new interview slot
def create_slot(request):
    error = None
    if request.method == 'POST':
        try:
            date = request.POST.get('date')
            time = request.POST.get('time')
            interviewer_name = request.POST.get('interviewer_name')
            job_role = request.POST.get('job_role')
            status = request.POST.get('status')
            
            InterviewSlot.objects.create(
                date=date,
                time=time,
                interviewer_name=interviewer_name,
                job_role=job_role,
                status=status
            )
            return redirect('slot_list')
        except Exception as e:
            error = f'Error creating slot: {str(e)}'
    
    return render(request, 'interviews/create_slot.html', {'error': error})

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

# Unassign an applicant from an interview slot
def unassign_interview(request, assignment_id):
    try:
        assignment = Assignment.objects.get(id=assignment_id)
        slot = assignment.interview_slot
        slot.status = 'Available'
        slot.save()
        assignment.delete()
        return redirect('assignment_list')
    except Assignment.DoesNotExist:
        return redirect('assignment_list')

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
