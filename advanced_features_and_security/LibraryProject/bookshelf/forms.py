from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'date_of_birth', 'profile_photo']
        widgets = {
            'password': forms.PasswordInput(),
        }

class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'date_of_birth', 'profile_photo']