from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    Form to specify fields in the user creation form
    """

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = 'Required. Letters, digits and @ . + - _ only.'

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('title', 'first_name', 'last_name', 'username', 'email', 'project')


class CustomUserChangeForm(UserChangeForm):
    """
    Form to specify fields in the user change form, which is only accessible via the Django admin
    """

    class Meta:
        model = CustomUser
        fields = ('title', 'first_name', 'last_name', 'username', 'email', 'project' )
