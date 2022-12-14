from django import forms
from accounts.models import UserModel
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(min_length=8, max_length=100, widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', max_length=100, widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data['email']
        user = UserModel.objects.filter(email=email).exists()
        if user:
            raise ValidationError('this email is already in use')
        return email

    def clean(self):
        password1 = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password2 == password1:
            return self.cleaned_data
        raise ValidationError('passwords are not much')


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
