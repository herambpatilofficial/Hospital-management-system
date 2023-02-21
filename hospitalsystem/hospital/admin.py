from django.contrib import admin

# Register your models here.
from django.urls import reverse
from django.utils.html import format_html
from .models import Doctor, Nurse, Ward



class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'phone_number', 'edit_button','assigned_patients')
    list_filter = ('name', 'specialization')
    def edit_button(self, obj):
        url = reverse('admin:hospital_doctor_change', args=[obj.id])
        return format_html('<a href="{}">Edit</a>', url)



admin.site.register(Doctor, DoctorAdmin)

class NurseAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'phone_number', 'ward', 'edit_button')
    list_filter = ('name', 'specialization', 'ward')
    def edit_button(self, obj):
        url = reverse('admin:hospital_nurse_change', args=[obj.id])
        return format_html('<a href="{}">Edit</a>', url)


admin.site.register(Nurse, NurseAdmin)


# Ward

class WardAdmin(admin.ModelAdmin):
    list_display = ('number', 'number_of_beds', 'edit_button', 'assigned_beds', 'assigned_nurses')
    list_filter = ('number', 'number_of_beds')
    def edit_button(self, obj):
        url = reverse('admin:hospital_ward_change', args=[obj.id])
        return format_html('<a href="{}">Edit</a>', url)

    # On clicking patient name, take to patient details page
   

admin.site.register(Ward, WardAdmin)