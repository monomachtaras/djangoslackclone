from django import forms
from .models import CustomUser


class UserCustomForm(forms.ModelForm):

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCustomForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'image',)
