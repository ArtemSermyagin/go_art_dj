from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER
from user.forms import RegisterForm
from user.models import User
from user.utils import generate_random_string


class UserRegisterView(CreateView):
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = form.save(commit=False)
        token = generate_random_string(24)
        user.is_active = False
        user.verification_token = token

        send_mail(
            "SkyStore!",
            "Перейдите по ссылке, чтобы завершить авторизацию",
            EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )

        user.save()
        return super().form_valid(form)
