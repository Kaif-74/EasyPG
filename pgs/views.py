from django.shortcuts import render, get_object_or_404
from .models import PG
from django.db.models import Q

def home(request):
    # Start with all PGs
    all_pgs = PG.objects.all().order_by('-created_at')
    
    # Get values from the URL (GET request)
    search_query = request.GET.get('search', '')
    category = request.GET.get('category', '')
    city_filter = request.GET.get('city', '') # Specific city dropdown/input
    sharing = request.GET.get('sharing', '')
    max_rent = request.GET.get('max_rent', '')

    # 1. Global Search (Checks Name, Area, Location, AND City)
    if search_query:
        all_pgs = all_pgs.filter(
            Q(name__icontains=search_query) | 
            Q(area__icontains=search_query) | 
            Q(location__icontains=search_query) |
            Q(city__icontains=search_query) # Added this line to fix your issue
        )

    # 2. Apply Specific Category Filter
    if category:
        all_pgs = all_pgs.filter(category=category)

    # 3. Apply Specific City Filter (If user used the specific city box)
    if city_filter:
        all_pgs = all_pgs.filter(city__icontains=city_filter)

    # 4. Apply Sharing Filter
    if sharing:
        all_pgs = all_pgs.filter(rooms__sharing_type=sharing).distinct()

    # 5. Apply Rent Filter
    if max_rent:
        all_pgs = all_pgs.filter(rooms__rent_per_bed__lte=max_rent).distinct()

    context = {
        'pgs': all_pgs,
        'values': request.GET 
    }
    return render(request, 'home.html', context)

def pg_detail(request, pg_id):
    pg = get_object_or_404(PG, id=pg_id)
    rooms = pg.rooms.all()
    return render(request, 'pg_detail.html', {'pg': pg, 'rooms': rooms})