from django.forms import ModelForm
from .models import Animacao,Terror,Comedia


class animacaoform(ModelForm):
    class Meta:
        model = Animacao
        fields =['filme','nota', 'imagem']

class terrorform(ModelForm):
    class Meta:
        model = Terror
        fields =['filme','nota', 'imagem']

class comediaform(ModelForm):
    class Meta:
        model = Comedia
        fields =['filme','nota', 'imagem']
