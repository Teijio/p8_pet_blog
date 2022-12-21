from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Skill, Message


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
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

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


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            "name",
            "email",
            "username",
            "location",
            "bio",
            "short_intro",
            "profile_image",
        ]
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = "__all__"
        exclude = ["owner"]
    
    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ["name", "email", "subject", "body"]

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        for k, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})