from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from . import models


class JournalEntryListView(ListView):
    """
    Class-based view to show the Journal Entry list template
    """

    template_name = 'journal/journalentry-list.html'
    model = models.JournalEntry
    paginate_by = 10


class JournalEntryDetailView(DetailView):
    """
    Class-based view to show the Journal Entry detail template
    """

    template_name = 'journal/journalentry-detail.html'
    model = models.JournalEntry


class JournalEntryCreateView(CreateView):
    """
    Class-based view to show the Journal Entry create template
    """

    template_name = 'journal/journalentry-create.html'
    fields = ['title', 'entry_text']
    model = models.JournalEntry


class JournalEntryUpdateView(UpdateView):
    """
    Class-based view to show the Journal Entry update template
    """

    template_name = 'journal/journalentry-update.html'
    fields = ['title', 'entry_text']
    model = models.JournalEntry


class JournalEntryDeleteView(DeleteView):
    """
    Class-based view to show the Journal Entry delete template
    """

    template_name = 'journal/journalentry-delete.html'
    model = models.JournalEntry
    success_url = reverse_lazy('journal-journalentry-list')
