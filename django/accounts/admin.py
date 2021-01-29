from django.contrib import admin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    """
    Display custom user in the Django admin
    """

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'title', 'first_name', 'last_name', 'username', 'project']
    list_filter = ['project', 'title']


admin.site.register(CustomUser, CustomUserAdmin)
