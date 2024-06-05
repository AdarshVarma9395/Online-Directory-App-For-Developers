from django.urls import path
from .views import *

urlpatterns = [
    path('', profiles, name = 'profiles'),
    path('profile/<str:pk>/', userProfile, name = 'user-profile'),
]
