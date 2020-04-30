from django.urls import path
from . import views

urlpatterns = [
    path('seekers/', views.seeker_list, name='seeker_list'),
    path('seeker/<int:pk>/', views.seeker_detail, name='seeker_detail'),
]
