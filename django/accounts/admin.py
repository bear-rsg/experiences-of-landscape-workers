from django.contrib import admin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Project, Title


class CustomUserAdmin(admin.ModelAdmin):
    """
    Display custom user in the Django admin
    """

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'title', 'first_name', 'last_name', 'username', 'project']
    list_filter = ['project', 'title']


class ProjectAdmin(admin.ModelAdmin):
    """
    Display projects in the Django admin
    """

    list_display = ['name', 'code', 'description', 'consent_message']


class TitleAdmin(admin.ModelAdmin):
    """
    Display titles in the Django admin
    """

    list_display = ['name']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Title, TitleAdmin)
