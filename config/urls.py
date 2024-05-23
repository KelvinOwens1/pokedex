from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views 


urlpatterns = [
    
    path("register/", registerPage, name="register"),
    path("login/", loginPage, name="login"),
    path("logout/", logoutUser, name="logout"),
    path('profile/', profile_page, name="profile"), 
    path("pokemon/", PokemonList.as_view(), name="pokemon"),
    path("pokemon_profile/<int:pk>", PokemonProfile.as_view(), name="pokemon_profile"),
    path("pokemon/add_pokemon", AddPokemon.as_view(), name="add_pokemon"),
    path("pokemon/update_pokemon/<int:pk>", UpdatePokemon.as_view(), name="update_pokemon"),
    path("pokemon/delete_pokemon/<int:pk>", DeletePokemon.as_view(), name="delete_pokemon"),
    path('random-pokemon/', random_pokemon_view, name='random_pokemon'),
    
    path("account/", account_settings, name="account"),
    path("", home_view, name="home"),
    path("admin/", admin.site.urls),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
