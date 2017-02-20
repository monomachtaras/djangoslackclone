from django import forms
from .models import CustomUser


class UserCusetomForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("image", )
