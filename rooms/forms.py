from django import forms
from .models import Room

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        # We exclude 'pg' because we will link it automatically in the view
        fields = [
            'room_number', 'floor_number', 'sharing_type', 'description',
            'total_beds', 'vacant_beds', 'rent_per_bed', 'security_deposit',
            'is_ac', 'has_attached_bathroom', 'has_balcony', 
            'has_wardrobe', 'has_study_table', 'has_fan'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 2}),
        }