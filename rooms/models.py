from django.db import models
from pgs.models import PG

class Room(models.Model):
    SHARING_CHOICES = [
        ('Single', 'Single Sharing'),
        ('Double', 'Double Sharing'),
        ('Triple', 'Triple Sharing'),
        ('Four', 'Four Sharing'),
        ('Five', 'Five Sharing'),
    ]

    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Fully Occupied', 'Fully Occupied'),
    ]

    # Link this room to a PG
    pg = models.ForeignKey(PG, on_delete=models.CASCADE, related_name='rooms')
    
    # Basic Room Info
    room_number = models.CharField(max_length=10)
    floor_number = models.IntegerField(default=0)
    sharing_type = models.CharField(max_length=20, choices=SHARING_CHOICES)
    description = models.TextField(blank=True, null=True)
    
    # Capacity and Pricing
    total_beds = models.PositiveIntegerField()
    vacant_beds = models.PositiveIntegerField()
    occupied_beds = models.PositiveIntegerField(default=0)
    rent_per_bed = models.DecimalField(max_digits=10, decimal_places=2)
    security_deposit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    # Room Facilities
    is_ac = models.BooleanField(default=False, verbose_name="AC Available")
    has_attached_bathroom = models.BooleanField(default=True)
    has_balcony = models.BooleanField(default=False)
    has_wardrobe = models.BooleanField(default=True)
    has_study_table = models.BooleanField(default=False)
    has_fan = models.BooleanField(default=True)
    
    # Status
    availability_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Available')
    
    # Timing
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Room {self.room_number} - {self.pg.name}"

class RoomImage(models.Model):
    """Gallery for each specific room"""
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_images')
    image = models.ImageField(upload_to='rooms/gallery/')

    def __str__(self):
        return f"Photo of Room {self.room.room_number}"