from .models import CastomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CastomUser
        # fields = UserCreationForm.Meta.fields + ('age',)
        fields = (
            'username', 'age', 'email', 'first_name', 'last_name',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CastomUser
        fields = (
            'username', 'age', 'email', 'first_name', 'last_name',)
