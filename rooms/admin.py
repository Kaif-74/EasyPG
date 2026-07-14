from django.contrib import admin
from .models import Room, RoomImage

class RoomImageInline(admin.TabularInline):
    model = RoomImage
    extra = 2

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'pg', 'sharing_type', 'vacant_beds', 'rent_per_bed', 'availability_status')
    list_filter = ('sharing_type', 'availability_status')
    search_fields = ('room_number', 'pg__name')
    inlines = [RoomImageInline]