from django.db import models
from django.contrib.auth.models import User

class PG(models.Model):
    # Category Choices
    CATEGORY_CHOICES = [
        ('Men', 'Men'),
        ('Women', 'Women'),
        ('Co-Living', 'Co-Living'),
    ]

    # Links this PG to a specific Owner (User)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_pgs')
    
    # Basic Information
    name = models.CharField(max_length=200)
    description = models.TextField()
    contact_number = models.CharField(max_length=15)
    
    # Address Details
    address = models.TextField()
    city = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    location = models.CharField(max_length=100, help_text="Specific locality name")
    google_maps_link = models.URLField(max_length=500, blank=True, null=True)
    
    # Categorization
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    
    # Media
    cover_image = models.ImageField(upload_to='pgs/covers/')
    
    # Facilities (True means it has the facility, False means it doesn't)
    has_parking = models.BooleanField(default=False)
    has_wifi = models.BooleanField(default=False)
    has_ro_water = models.BooleanField(default=False)
    has_food = models.BooleanField(default=False)
    has_laundry = models.BooleanField(default=False)
    has_cleaning = models.BooleanField(default=False)
    has_power_backup = models.BooleanField(default=False)
    has_cctv = models.BooleanField(default=False)
    has_security_guard = models.BooleanField(default=False)

    # Timing
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class PGImage(models.Model):
    """Allowing multiple images for one PG"""
    pg = models.ForeignKey(PG, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='pgs/gallery/')

    def __str__(self):
        return f"Image for {self.pg.name}"