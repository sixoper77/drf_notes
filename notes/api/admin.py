from django.contrib import admin
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    readonly_fields=['created_at','updated_at']
    search_fields=[
        'name',
        'subtask'
    ]
    list_display=[
        'name',
        'created_at',
        'updated_at'
    ]
    list_filtet=[
        'created_at',
        'updated_at'
    ]
    
