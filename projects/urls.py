from django.urls import path
from .views import *

urlpatterns = [
    path("", projects, name='projects'),
    path("single-project/<str:pk>/", singleProject, name='single-project'),
]