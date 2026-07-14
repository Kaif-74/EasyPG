from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),
    path('admin-panel/', views.admin_dashboard, name='admin_dashboard'),
    path('profile/', views.profile_settings, name='profile_settings'),
    path('add-pg/', views.add_pg, name='add_pg'),
    path('edit-pg/<int:pg_id>/', views.edit_pg, name='edit_pg'),
    path('delete-pg/<int:pg_id>/', views.delete_pg, name='delete_pg'),
    path('pg-images/<int:pg_id>/', views.manage_pg_images, name='manage_pg_images'),
    path('delete-pg-image/<int:image_id>/', views.delete_pg_image, name='delete_pg_image'),
    path('manage-rooms/<int:pg_id>/', views.manage_rooms, name='manage_rooms'),
    path('add-room/<int:pg_id>/', views.add_room, name='add_room'),
    path('edit-room/<int:room_id>/', views.edit_room, name='edit_room'),
    path('delete-room/<int:room_id>/', views.delete_room, name='delete_room'),
    path('update-vacancy/<int:room_id>/', views.update_vacancy, name='update_vacancy'),
    path('room-images/<int:room_id>/', views.manage_room_images, name='manage_room_images'),
    path('delete-room-image/<int:image_id>/', views.delete_room_image, name='delete_room_image'),
]