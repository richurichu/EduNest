from django.urls import path,include
from .views import *


urlpatterns = [
    path('notes/', NoteListCreateView.as_view(), name='note-list-create'),
    path('notes-list/', AllNotesListView.as_view(), name='all-notes-list'),
    
]