from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib import messages

from .models import *
from .forms import CreateUserForm, Trainer_form, PokemonForm
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.urls import reverse_lazy
import random


class PokemonList(ListView):
    model = Pokemon
    template_name = 'pokemon.html'
    ordering = ['id']


class PokemonProfile(DetailView):
    model = Pokemon
    template_name = 'pokemon_profile.html'


# @login_required(login_url='login')
# @allowed_users(allowed_roles='admin')
class AddPokemon(CreateView):
    model = Pokemon
    form_class = PokemonForm
    template_name = "add_pokemon.html"
    # fields = ("num", "name")
    success_url = reverse_lazy('pokemon')


class UpdatePokemon(UpdateView):
    model = Pokemon
    form_class = PokemonForm
    template_name = "add_pokemon.html"
    success_url = reverse_lazy('pokemon')


class DeletePokemon(DeleteView):
    model = Pokemon
    template_name = "delete_pokemon.html"
    success_url = reverse_lazy('pokemon')    



def home_view(request):
    
    trainers = Trainer.objects.all()
    pokemon_list = Pokemon.objects.all()

    total_trainers = trainers.count()

    total_pokemon = pokemon_list.count()

    context = {"trainers": trainers, "total_trainers": total_trainers, "total_pokemon": total_pokemon,}

    return render(request, "home.html", context)


def random_pokemon_view(request):
    pk_list = list(Pokemon.objects.values_list('id', flat=True))
    if pk_list:
        random_pk = random.choice(pk_list)
        return redirect('pokemon_profile', pk=random_pk)
    else:
        return redirect('home')


def logoutUser(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
# @allowed_users(allowed_roles=['trainer', 'admin'])
def profile_page(request):
    trainer2 = Trainer.objects.all()
    context = {"trainer2": trainer2}
    return render(request, "profile.html", context)


@login_required(login_url='login')
# @allowed_users(allowed_roles=['trainer', 'admin'])
def account_settings(request):
    trainer_settings = request.user.trainer
    form = Trainer_form(instance=trainer_settings)

    if request.method == 'POST':
        form = Trainer_form(request.POST, request.FILES, instance=trainer_settings)
        if form.is_valid():
            form.save()


    context = {"form": form}
    return render(request, "accounts/account_settings.html", context)
