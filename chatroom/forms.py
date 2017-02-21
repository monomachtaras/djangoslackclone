from django import forms
from django.core.mail import send_mail
from .models import CustomUser
from django.utils.crypto import get_random_string
from hashlib import sha256


def send_email(data):
    message = r'activate/' + data['activation_key']
    message += '\n не забудьте додати localhost:port'
    send_mail('Activation link', message, 'volodymyrfilsg@gmail.com', [data['user_mail']])


def generate_key(username):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    secret_key = get_random_string(20, chars)
    return sha256((secret_key + username).encode('utf-8')).hexdigest()


class UserCustomForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCustomForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.is_active = False
        user.activation_key = generate_key(user.username)
        data = {'activation_key' : user.activation_key, 'user_mail' : user.email}
        send_email(data)
        if commit:
            user.save()
        return user

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'image',)
