
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm as DjangoPasswordChangeForm
from django.contrib.auth.forms import UserCreationForm
from .models import  Stage, Evenement, Logement, Transport

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email')



class PasswordChangeForm(DjangoPasswordChangeForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)



class StageForm(forms.ModelForm):
    class Meta:
        model = Stage
        fields = ['title', 'content', 'type', 'stage_type']

class LogementForm(forms.ModelForm):
    class Meta:
        model = Logement
        fields = ['title', 'content', 'type', 'address', 'price']

class EvenementForm(forms.ModelForm):
    class Meta:
        model = Evenement
        fields = ['title', 'content', 'type', 'description', 'event_type', 'price']

class TransportForm(forms.ModelForm):
    class Meta:
        model = Transport
        fields = ['title', 'content', 'type', 'destination']
