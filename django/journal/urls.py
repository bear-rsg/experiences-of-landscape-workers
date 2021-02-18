from django.urls import path
from . import views

urlpatterns = [
    path('', views.JournalEntryListView.as_view(), name='journal-journalentry-list'),
    path('create/', views.JournalEntryCreateView.as_view(), name='journal-journalentry-create'),
    path('update/<pk>/', views.JournalEntryUpdateView.as_view(), name='journal-journalentry-update'),
    path('delete/<pk>/', views.JournalEntryDeleteView.as_view(), name='journal-journalentry-delete'),
    path('<pk>/', views.JournalEntryDetailView.as_view(), name='journal-journalentry-detail'),
]
