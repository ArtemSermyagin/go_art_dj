from django.contrib.auth.views import LoginView, PasswordResetView
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER, BASE_DOMAIN
from user.forms import RegisterForm, AuthenticationForm
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
            f"Перейдите по ссылке, чтобы завершить авторизацию: {BASE_DOMAIN}{reverse('verification-email', args=(token,))}",
            EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )

        user.save()
        return super().form_valid(form)


class UserVerificationView(View):

    def get(self, request, *args, **kwargs):
        token = kwargs['token']
        try:
            user = User.objects.get(verification_token=token)
        except User.DoesNotExist:
            raise Http404("Token not found")
        user.is_active = True
        user.save()
        return redirect("login")


class UserLoginView(LoginView):
    form_class = AuthenticationForm
    success_url = reverse_lazy("home")
    template_name = 'user/user_login.html'


class RestorePasswordUserView(PasswordResetView):
    template_name = 'user/restore_password.html'

    def post(self, request, *args, **kwargs):
        user: User = get_object_or_404(User, email=request.POST.get('email'))
        new_password = generate_random_string(20)
        send_mail(
            "SkyStore!",
            f"Ваш новый пароль: {new_password}",
            EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )
        user.set_password(new_password)
        user.save()
        return redirect('login')
