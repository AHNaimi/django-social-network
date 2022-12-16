from django.shortcuts import render, redirect
from django.views import View
from accounts.forms import RegisterForm, LoginForm
from accounts.models import UserModel
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin


class RegisterView(View):
    form_class = RegisterForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:homepage')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, 'accounts/register.html', {"form": self.form_class})

    def post(self, request):
        form_post = self.form_class(request.POST)
        if form_post.is_valid():
            form_valid = form_post.cleaned_data
            user = UserModel.objects.create_user(form_valid['email'], form_valid['full_name'], form_valid['password'])
            user.save()
            login(request, user)
            return redirect('home:homepage')
        return render(request, 'accounts/register.html', {"form": form_post})


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('home:homepage')


class LoginView(View):
    form_class = LoginForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:homepage')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, 'accounts/login.html', {'form': self.form_class})

    def post(self, request):
        post_form = self.form_class(request.POST)
        if post_form.is_valid():
            form_valid = post_form.cleaned_data
            user = authenticate(request, username=form_valid['email'], password=form_valid['password'])
            if user is not None:
                login(request, user)
                return redirect('home:homepage')
            return render(request, 'accounts/login.html', {'form': post_form})
        return render(request, 'accounts/login.html', {'form': post_form})



