from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Patient
# Import requests
import requests


# Create your views here.

class PatientListView(ListView):
    model = Patient
    template_name = 'patients/patient_list.html'
    context_object_name = 'patients'
   



