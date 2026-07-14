from django.contrib import admin
from .models import PG, PGImage

class PGImageInline(admin.TabularInline):
    model = PGImage
    extra = 3

@admin.register(PG)
class PGAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'city', 'area', 'owner', 'created_at')
    list_filter = ('category', 'city')
    search_fields = ('name', 'city', 'area')
    inlines = [PGImageInline]