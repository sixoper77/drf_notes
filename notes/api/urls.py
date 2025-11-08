from django.urls import path

from . import views
app_name='api'

urlpatterns = [
    path('api/register/',views.RegistrationAPIView.as_view()),
    path('api/notes/',views.CreateListAPIView.as_view()),
    path('api/notes/<int:pk>/',views.NoteDetailAPIView.as_view())
]
