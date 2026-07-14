from django.contrib import admin
from .models import OwnerProfile

@admin.register(OwnerProfile)
class OwnerProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'mobile_number', 'user', 'created_at')
    search_fields = ('full_name', 'mobile_number')