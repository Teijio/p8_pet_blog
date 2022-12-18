from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# мы изменяем стандартную форму регистрации, по умолчанию у нас был только
# логин и пароль
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "email",
            "username",
            "password1",
            "password2",
        ]
        labels = {
            "first_name": "Name",
        }
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        
        self.fields["first_name"].widget.attrs.update(
            {"class": "input", "placeholder": "Enter your Name"}
        )
        self.fields["email"].widget.attrs.update(
            {"class": "input", "placeholder": "Enter your email"}
        )
        self.fields["username"].widget.attrs.update(
            {"class": "input", "placeholder": "Enter your username"}
        )
        self.fields["password1"].widget.attrs.update(
            {"class": "input", "placeholder": "••••••••"}
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "input", "placeholder": "••••••••"}
        )
