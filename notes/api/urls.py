from django.urls import path
from .serializers import Notes
from . import views
app_name='api'

urlpatterns = [
    path('notes/',views.get_notes)
]
