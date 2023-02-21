from django.contrib import admin

# Register your models here.
from django.urls import reverse
from django.utils.html import format_html


from .models import Patient




# admin.site.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "date_of_birth", "city", "blood_type", "age", 'edit_button', 'delete_button')
    list_filter = ("city", "blood_type")
    search_fields = ("first_name", "last_name", "city", "blood_type")
    def edit_button(self, obj):
        url = reverse('admin:patients_patient_change', args=[obj.id])
        return format_html('<a href="{}">Edit</a>', url)

    def delete_button(self, obj):
        url = reverse('admin:patients_patient_delete', args=[obj.id])
        return format_html('<a href="{}">Delete</a>', url)


admin.site.register(Patient, PatientAdmin)

hosp_name = "Turing TechLabs Hospital"


admin.site.site_header  =  f"{hosp_name} Site"  
admin.site.site_title  =  f"{hosp_name} Admin Portal"
admin.site.index_title  =  f"Welcome to {hosp_name} Portal"


from  django.contrib.auth.models  import  Group  
admin.site.unregister(Group) 








