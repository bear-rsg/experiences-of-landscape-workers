from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models


class JournalEntryListView(LoginRequiredMixin, ListView):
    """
    Class-based view to show the Journal Entry list template
    """

    template_name = 'journal/journalentry-list.html'
    model = models.JournalEntry
    paginate_by = 10

    def get_queryset(self):
        return models.JournalEntry.objects.filter(
            user=self.request.user
        ).order_by('-meta_created_datetime')


class JournalEntryDetailView(LoginRequiredMixin, DetailView):
    """
    Class-based view to show the Journal Entry detail template
    """

    template_name = 'journal/journalentry-detail.html'
    model = models.JournalEntry

    def get_queryset(self):
        return models.JournalEntry.objects.filter(
            user=self.request.user
        )


class JournalEntryCreateView(LoginRequiredMixin, CreateView):
    """
    Class-based view to show the Journal Entry create template
    """

    template_name = 'journal/journalentry-create.html'
    fields = ['title', 'entry_text']
    model = models.JournalEntry

    def form_valid(self, form):
        """
        Adds the current user from the request as the 'user' field for this new object
        """
        user = self.request.user
        form.instance.user = user
        return super(JournalEntryCreateView, self).form_valid(form)


class JournalEntryUpdateView(LoginRequiredMixin, UpdateView):
    """
    Class-based view to show the Journal Entry update template
    """

    template_name = 'journal/journalentry-update.html'
    fields = ['title', 'entry_text']
    model = models.JournalEntry


class JournalEntryDeleteView(LoginRequiredMixin, DeleteView):
    """
    Class-based view to show the Journal Entry delete template
    """

    template_name = 'journal/journalentry-delete.html'
    model = models.JournalEntry
    success_url = reverse_lazy('journal-journalentry-list')
