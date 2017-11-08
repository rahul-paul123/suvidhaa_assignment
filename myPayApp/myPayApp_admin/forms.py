from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from myPayApp_admin import models as adminModels

class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'gui-input','placeholder': 'Enter Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'gui-input','placeholder':'Enter Password'}))

class UserProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = 'Email'
        self.fields['username'].label = 'Username'

    class Meta:
        model = adminModels.UserProfile
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class BillerProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BillerProfileForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = 'Email'
        self.fields['username'].label = 'Username'

    class Meta:
        model = adminModels.BillerProfile
        fields = ['first_name', 'last_name', 'email', 'username', 'password',
                  'bill_type']
        widgets = {
            'password': forms.PasswordInput(),
        }