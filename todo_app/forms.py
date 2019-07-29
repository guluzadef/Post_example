from django import forms
from .models import Contact, Profil, Article, UserSetting
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Article
        fields = ["title", "description", "image", "content"]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "description": forms.TextInput(attrs={
                "class": "form-control"
            })
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            "name", "email",
            "number", "message"]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),
            "number": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Number"}),
            "message": forms.TextInput(attrs={"class": "form-control", "placeholder": "Message"}),

        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control"
        }

    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class": "form-control"
        }

    ))


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class": "form-control"
        }))
    profile_image = forms.ImageField(widget=forms.FileInput(
        attrs={
            "class": "form-control"
        }
    ))
    background_image = forms.ImageField(widget=forms.FileInput(
        attrs={
            "class": "form-control"
        }
    ))

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]
        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "last_name": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "username": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control"
            }),

        }


class ProfileForm(forms.ModelForm):
    profile_image = forms.ImageField(widget=forms.FileInput(
        attrs={
            "class": "form-control"
        }
    ))
    background_image = forms.ImageField(widget=forms.FileInput(
        attrs={
            "class": "form-control"
        }
    ))

    class Meta:
        model = Profil
        fields = ["user", "profile_image", "background_image", "about"]


class SettingsForm(forms.ModelForm):
    about = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control"
    }))
    profile_image = forms.ImageField(required=False, widget=forms.FileInput(attrs={
        "class": "form-control"
    }))
    background_image = forms.ImageField(required=False, widget=forms.FileInput(attrs={
        "class": "form-control"
    }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class": "form-control"
        }))

    class Meta:
        model = User
        fields = ["first_name", "last_name"]
        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "last_name": forms.TextInput(attrs={
                "class": "form-control"
            }),

        }
