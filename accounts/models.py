from django.db import models
from django.contrib.auth.models import User

class OwnerProfile(models.Model):
    # This links the profile to the built-in Django User account
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    # Extra fields for the owner
    full_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15, unique=True)
    
    # Timing
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name