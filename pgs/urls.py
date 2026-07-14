from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pg/<int:pg_id>/', views.pg_detail, name='pg_detail'),
]