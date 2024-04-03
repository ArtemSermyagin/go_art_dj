from django.contrib.auth.forms import UserCreationForm

from catalog.forms import FormStyleMixin
from user.models import User


class RegisterForm(FormStyleMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password')
