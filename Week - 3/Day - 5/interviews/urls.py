from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('applicants/', views.applicant_list, name='applicant_list'),
    path('slots/', views.slot_list, name='slot_list'),
    path('slots/create/', views.create_slot, name='create_slot'),
    path('assignments/', views.assignment_list, name='assignment_list'),
    path('assign/', views.assign_interview, name='assign_interview'),
    path('slots/<int:slot_id>/update_status/', views.update_slot_status, name='update_slot_status'),
    path('assignments/<int:assignment_id>/unassign/', views.unassign_interview, name='unassign'),
]
