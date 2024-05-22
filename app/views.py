from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView

from django.contrib import messages

from .models import *
from .forms import CreateUserForm, Trainer_form
from .decorators import unauthenticated_user, allowed_users, admin_only


class PokemonList(ListView):
    model = Pokemon
    template_name = 'pokemon.html'


class PokemonProfile(DetailView):
    model = Pokemon
    template_name = 'pokemon_profile.html'


def home_view(request):
    
    trainers = Trainer.objects.all()
    pokemon_list = Pokemon.objects.all()

    total_trainers = trainers.count()

    total_pokemon = pokemon_list.count()

    context = {"trainers": trainers, "total_trainers": total_trainers, "total_pokemon": total_pokemon}

    return render(request, "home.html", context)


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")

            messages.success(request, "User account has been created for " + username)

            return redirect("login")

    context = {'form' : form}
    return render(request, "accounts/register.html", context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.info(request, "Username or Password incorrect.")

    context = {}
    return render(request, "accounts/login.html", context)


def logoutUser(request):
    logout(request)
    return redirect('login')


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
