from django.views.generic import CreateView

from user.forms import RegisterForm
from user.models import User


class UserRegisterView(CreateView):
    model = User
    form_class = RegisterForm
