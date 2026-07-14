from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from pgs.models import PG, PGImage
from pgs.forms import PGForm
from rooms.models import Room, RoomImage
from rooms.forms import RoomForm
from accounts.models import OwnerProfile
from accounts.forms import ProfileForm
from django.contrib import messages

@login_required
def dashboard_home(request):
    # If Superuser, send to Admin Panel
    if request.user.is_superuser:
        return redirect('admin_dashboard')
        
    my_pgs = PG.objects.filter(owner=request.user).order_by('-created_at')
    return render(request, 'dashboard/home.html', {'pgs': my_pgs})

@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return redirect('home')

    context = {
        'total_owners': OwnerProfile.objects.count(),
        'total_pgs': PG.objects.count(),
        'total_rooms': Room.objects.count(),
        'all_owners': OwnerProfile.objects.all().order_by('-created_at'),
        'all_pgs': PG.objects.all().order_by('-created_at'),
    }
    return render(request, 'dashboard/admin_home.html', context)

@login_required
def profile_settings(request):
    try:
        profile = request.user.profile
    except:
        messages.error(request, "Admins do not have an editable owner profile.")
        return redirect('admin_dashboard')

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated!")
            return redirect('dashboard_home')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'dashboard/profile.html', {'form': form})

@login_required
def add_pg(request):
    if request.method == 'POST':
        form = PGForm(request.POST, request.FILES)
        if form.is_valid():
            pg = form.save(commit=False)
            pg.owner = request.user
            pg.save()
            messages.success(request, "PG added successfully!")
            return redirect('dashboard_home')
    else:
        form = PGForm()
    return render(request, 'dashboard/add_pg.html', {'form': form})

@login_required
def edit_pg(request, pg_id):
    # Admins can edit any PG, Owners only their own
    if request.user.is_superuser:
        pg = get_object_or_404(PG, id=pg_id)
    else:
        pg = get_object_or_404(PG, id=pg_id, owner=request.user)

    if request.method == 'POST':
        form = PGForm(request.POST, request.FILES, instance=pg)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated!")
            return redirect('dashboard_home')
    else:
        form = PGForm(instance=pg)
    return render(request, 'dashboard/edit_pg.html', {'form': form, 'pg': pg})

@login_required
def delete_pg(request, pg_id):
    if request.user.is_superuser:
        pg = get_object_or_404(PG, id=pg_id)
    else:
        pg = get_object_or_404(PG, id=pg_id, owner=request.user)
        
    if request.method == 'POST':
        pg.delete()
        messages.success(request, "Deleted!")
        return redirect('dashboard_home')
    return render(request, 'dashboard/confirm_delete.html', {'item': pg, 'type': 'PG'})

@login_required
def manage_pg_images(request, pg_id):
    pg = get_object_or_404(PG, id=pg_id)
    if not request.user.is_superuser and pg.owner != request.user:
        return redirect('home')
    if request.method == 'POST':
        for img in request.FILES.getlist('images'):
            PGImage.objects.create(pg=pg, image=img)
        return redirect('manage_pg_images', pg_id=pg.id)
    return render(request, 'dashboard/manage_pg_images.html', {'pg': pg, 'images': pg.images.all()})

@login_required
def delete_pg_image(request, image_id):
    image = get_object_or_404(PGImage, id=image_id)
    pg_id = image.pg.id
    image.delete()
    return redirect('manage_pg_images', pg_id=pg_id)

@login_required
def manage_rooms(request, pg_id):
    pg = get_object_or_404(PG, id=pg_id)
    return render(request, 'dashboard/manage_rooms.html', {'pg': pg, 'rooms': Room.objects.filter(pg=pg)})

@login_required
def add_room(request, pg_id):
    pg = get_object_or_404(PG, id=pg_id)
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.pg = pg
            room.availability_status = 'Available' if room.vacant_beds > 0 else 'Fully Occupied'
            room.save()
            return redirect('manage_rooms', pg_id=pg.id)
    else:
        form = RoomForm()
    return render(request, 'dashboard/add_room.html', {'form': form, 'pg': pg})

@login_required
def edit_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('manage_rooms', pg_id=room.pg.id)
    else:
        form = RoomForm(instance=room)
    return render(request, 'dashboard/edit_room.html', {'form': form, 'room': room})

@login_required
def delete_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    pg_id = room.pg.id
    if request.method == 'POST':
        room.delete()
        return redirect('manage_rooms', pg_id=pg_id)
    return render(request, 'dashboard/confirm_delete.html', {'item': room, 'type': 'Room'})

@login_required
def update_vacancy(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        room.vacant_beds = int(request.POST.get('vacant_beds'))
        room.availability_status = 'Available' if room.vacant_beds > 0 else 'Fully Occupied'
        room.save()
        return redirect('manage_rooms', pg_id=room.pg.id)
    return render(request, 'dashboard/update_vacancy.html', {'room': room})

@login_required
def manage_room_images(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        for img in request.FILES.getlist('images'):
            RoomImage.objects.create(room=room, image=img)
        return redirect('manage_room_images', room_id=room.id)
    return render(request, 'dashboard/manage_room_images.html', {'room': room, 'images': room.room_images.all()})

@login_required
def delete_room_image(request, image_id):
    image = get_object_or_404(RoomImage, id=image_id)
    room_id = image.room.id
    image.delete()
    return redirect('manage_room_images', room_id=room_id)