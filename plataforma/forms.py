from django import forms
from django.db import models
from django.forms.fields import CharField, EmailField, IntegerField
from .models import Livros

class Livro(forms.ModelForm):
    class Meta:
        model = Livros
        fields = "__all__"

class FormTeste(forms.Form):
    nome = CharField(max_length=20)
    email = EmailField()
    id = IntegerField()
    