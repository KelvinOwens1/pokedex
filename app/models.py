from django.db import models
from django.contrib.auth.models import User
    

class Pokemon_types(models.Model):
    pokemon_types = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.pokemon_types
    

class Pokemon(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    num = models.CharField(max_length=4)
    name = models.CharField(max_length=50)
    pokemon_types = models.ManyToManyField(Pokemon_types, related_name="type", related_query_name="types", null=True)
    description = models.TextField(null=True)
    evolutions = models.TextField(null=True)
    pokemon_pic = models.ImageField(default=None, null=True, blank=True)

    def __str__(self):
        return self.name
    

class Trainer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50, null=True, default="Name")
    name = models.CharField(max_length=50, default="Full Name")
    profile_pic = models.ImageField(default='avatar_6388000.png', null=True, blank=True)
    pokedex = models.ForeignKey(Pokemon, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
