from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import Extras, Libro, Extras
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LibroForm(ModelForm):

    nombre = forms.CharField(min_length=2, max_length=200)

    class Meta:
        model=Libro
        fields = ['nombre','autor','año','genero','sinopsis','num_pag','precio','imprenta','imagen','cantidad']


class CustomUserForm(UserCreationForm):

    class Meta:
        model = User 
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class ExtraForms(ModelForm):

    class Meta:
        model = Extras
        fields = ['imagen_per', 'edad']