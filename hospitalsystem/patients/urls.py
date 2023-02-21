# URLS
from .views import PatientListView
from django.urls import path
# PatientDetailView, PatientCreateView, PatientUpdateView, PatientDeleteView

urlpatterns = [
     path('', PatientListView.as_view(), name='patient_list'),
     
]
