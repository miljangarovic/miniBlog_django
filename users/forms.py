from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
from .models import Profile



class CustomUserCreationForm(UserCreationForm): #naslijedimo UserCreationForm
    class Meta:
        model = User
        fields=['first_name','email','username','password1','password2']
        labels = {
            'first_name':'Name',
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)



        self.fields['first_name'].widget.attrs.update(
            {'class': 'input input--text', 'placeholder': 'e.g. Miljan Garovic'})  # ovako smo polju title promijenili klasu
        self.fields['email'].widget.attrs.update({'class': 'input input--email', 'placeholder': 'Add description'})
        self.fields['username'].widget.attrs.update({'class': 'input input--password', 'placeholder': 'Enter Username'})
        self.fields['password1'].widget.attrs.update({'class': 'input input--password', 'placeholder': 'Enter Password'})
        self.fields['password2'].widget.attrs.update({'class': 'input input--password', 'placeholder': 'Confrim Password'})

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','email','username','profile_image','location','bio','social_github','social_twitter',
                  'social_website','social_youtube','social_linkedin']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)



        self.fields['name'].widget.attrs.update({'class': 'input',})  # ovako smo polju title promijenili klasu
        self.fields['email'].widget.attrs.update({'class': 'input',})  # ovako smo polju title promijenili klasu
        self.fields['username'].widget.attrs.update({'class': 'input',})  # ovako smo polju title promijenili klasu
        self.fields['profile_image'].widget.attrs.update({'class': 'input',})  # ovako smo polju title promijenili klasu
        self.fields['location'].widget.attrs.update({'class': 'input',})  # ovako smo polju title promijenili klasu
        self.fields['bio'].widget.attrs.update({'class': 'input',})  # ovako smo polju title promijenili klasu
        self.fields['social_github'].widget.attrs.update({'class': 'input',})  # ovako smo polju title promijenili klasu
        self.fields['social_twitter'].widget.attrs.update({'class': 'input',})  # ovako smo polju title promijenili klasu
        self.fields['social_website'].widget.attrs.update({'class': 'input',})  # ovako smo polju title promijenili klasu
        self.fields['social_youtube'].widget.attrs.update({'class': 'input',})  # ovako smo polju title promijenili klasu
        self.fields['social_linkedin'].widget.attrs.update({'class': 'input',})  # ovako smo polju title promijenili klasu
