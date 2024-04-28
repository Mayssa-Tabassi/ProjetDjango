from django.shortcuts import render,redirect,HttpResponseRedirect
from .forms import UserCreationForm,UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView
from .forms import StageForm, LogementForm, EvenementForm, TransportForm
from .models import Stage, Logement, Evenement, Transport

# Create your views here.


def acceuil(request):
        return render(request, 'acceuil.html')

def inscription(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès!')
            return redirect('acceuil')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/inscription.html', {'form': form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Met à jour la session de l'utilisateur pour éviter la déconnexion
            messages.success(request, 'Votre mot de passe a été changé avec succès!')
            return redirect('acceuil')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'registration/change_password.html', {'form': form})


class StageCreateView(CreateView):
    model = Stage
    form_class = StageForm
    template_name = 'forms/stage_form.html'
    success_url = reverse_lazy()# Mettez à jour avec votre URL de succès

class LogementCreateView(CreateView):
    model = Logement
    form_class = LogementForm
    template_name = 'forms/logement_form.html'
    success_url = reverse_lazy() # Mettez à jour avec votre URL de succès

class EvenementCreateView(CreateView):
    model = Evenement
    form_class = EvenementForm
    template_name = 'forms/evenement_form.html'
    success_url = reverse_lazy()  # Mettez à jour avec votre URL de succès

class TransportCreateView(CreateView):
    model = Transport
    form_class = TransportForm
    template_name = 'forms/transport_form.html'
    success_url = reverse_lazy() # Mettez à jour avec votre URL de succès




def LogementList(request):
    return render(request, 'List/logementList.html')



def EventList(request):
    return render(request, 'List/EventList.html')


def StageList(request):
    return render(request, 'List/StageList.html')


def TransportList(request):
    return render(request, 'List/TransportList.html')


