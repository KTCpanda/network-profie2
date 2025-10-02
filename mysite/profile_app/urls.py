# profile_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_view, name='profile'),
    path('edit/', views.profile_edit_view, name='profile_edit'),
]