from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from . import models


class JournalEntryListView(LoginRequiredMixin, ListView):
    """
    Class-based view to show the Journal Entry list template
    """

    template_name = 'journal/journalentry-list.html'
    model = models.JournalEntry

    def get_queryset(self):

        # Limit the objects to that of the logged in user only
        queryset = models.JournalEntry.objects.filter(
            user=self.request.user
        ).order_by('-meta_created_datetime')

        # Filter based on search (if provided)
        search = self.request.GET.get('search', '')
        if search != '':
            queryset = queryset.filter(
                Q(id__contains=search) |
                Q(title__contains=search) |
                Q(entry_text__contains=search)
            )

        return queryset


class JournalEntryDetailView(LoginRequiredMixin, DetailView):
    """
    Class-based view to show the Journal Entry detail template
    """

    template_name = 'journal/journalentry-detail.html'
    model = models.JournalEntry

    def get_queryset(self):
        """
        Limit the object to that of the logged in user only
        """
        return models.JournalEntry.objects.filter(
            user=self.request.user
        )


class JournalEntryCreateView(LoginRequiredMixin, CreateView):
    """
    Class-based view to show the Journal Entry create template
    """

    template_name = 'journal/journalentry-create.html'
    fields = ['entry_text', 'entry_image']
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
    fields = ['entry_text', 'entry_image']
    model = models.JournalEntry

    def get_queryset(self):
        """
        Limit the object to that of the logged in user only
        """
        return models.JournalEntry.objects.filter(
            user=self.request.user
        )


class JournalEntryDeleteView(LoginRequiredMixin, DeleteView):
    """
    Class-based view to show the Journal Entry delete template
    """

    template_name = 'journal/journalentry-delete.html'
    model = models.JournalEntry
    success_url = reverse_lazy('journal-journalentry-list')

    def get_queryset(self):
        """
        Limit the object to that of the logged in user only
        """
        return models.JournalEntry.objects.filter(
            user=self.request.user
        )


class JournalEntryDraftsTemplateView(TemplateView):
    """
    Class-based view to show the Journal Entry drafts template
    """

    template_name = 'journal/journalentry-drafts.html'
