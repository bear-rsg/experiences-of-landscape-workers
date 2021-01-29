from django.views.generic import (TemplateView, CreateView)
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm


class AccountProfileTemplateView(TemplateView):
    """
    Class-based view to show the account profile template
    """

    template_name = 'account/account-profile.html'


class AccountCreateView(CreateView):
    """
    Class-based view to show the account create template
    """

    template_name = 'account/account-create.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
