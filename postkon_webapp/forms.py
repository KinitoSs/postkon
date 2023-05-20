from black import err
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from postkon_webapp.models import Post, Profile
from django.core.exceptions import ValidationError


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


def validate_email(value):
    if User.objects.filter(email=value).exists():
        raise ValidationError((f"{value} уже занят."), params={"value": value})


class RegisterForm(UserCreationForm):
    # username = forms.CharField()
    birthday = forms.DateField(
        required=True,
        label="Дата рождения",
        widget=forms.DateInput(attrs={"type": "date"}),
    )
    email = forms.EmailField(validators=[validate_email])
    password1 = forms.CharField(widget=forms.PasswordInput, label="Введите пароль")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Повторите пароль")

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "birthday",
            "password1",
            "password2",
        )


class SettingsForm(forms.ModelForm):
    first_name = forms.CharField(required=False, label="Имя")
    last_name = forms.CharField(required=False, label="Фамилия")

    class Meta:
        model = User
        fields = ("first_name", "last_name")


class ProfileSettingsForm(forms.ModelForm):
    status = forms.CharField(required=False, label="Статус")
    avatar_img = forms.CharField(required=False, label="Ссылка на изображение")
    # birthday = forms.DateField(
    #     required=True, label='Дата рождения', widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Profile
        fields = ("status", "avatar_img")
