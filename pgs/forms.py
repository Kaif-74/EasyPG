from django import forms
from .models import PG

class PGForm(forms.ModelForm):
    class Meta:
        model = PG
        # We exclude 'owner' because we will assign it automatically in the view
        fields = [
            'name', 'description', 'contact_number', 'address', 
            'city', 'area', 'location', 'google_maps_link', 
            'category', 'cover_image', 'has_parking', 'has_wifi', 
            'has_ro_water', 'has_food', 'has_laundry', 'has_cleaning', 
            'has_power_backup', 'has_cctv', 'has_security_guard'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'address': forms.Textarea(attrs={'rows': 3}),
        }