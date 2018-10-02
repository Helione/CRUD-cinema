from django.urls import path
from .views import list_filmes_comedia, list_filmes_animacao, list_filmes_terror
from .views import filmes,nova_comedia,nova_animacao,nova_terror
from .views import atualizar_comedia, atualizar_animacao, atualizar_terror
from .views import deletar_comedia,deletar_animacao, deletar_terror

urlpatterns = [
    path('filmes', filmes, name='filmes'),
    path('listfilmecomedia/', list_filmes_comedia, name='list_filmes_comedia'),
    path('listfilmeanimacao/', list_filmes_animacao, name='list_filmes_animacao'),
    path('listfilmeterror/', list_filmes_terror, name='list_filmes_terror'),
    path('comedia/', nova_comedia, name='nova_comedia'),
    path('animacao/', nova_animacao, name='nova_animacao'),
    path('terror/', nova_terror, name='nova_terror'),
    path('atualizarcomedia/<int:id>/', atualizar_comedia, name='atualizar_comedia'),
    path('deletarcomedia/<int:id>/', deletar_comedia, name='deletar_comedia'),
    path('atualizaranimacao/<int:id>/', atualizar_animacao, name='atualizar_animacao'),
    path('deletaranimacao/<int:id>/', deletar_animacao, name='deletar_animacao'),
    path('atualizarterror/<int:id>/', atualizar_terror, name='atualizar_terror'),
    path('deletarterror/<int:id>/', deletar_terror, name='deletar_terror'),
]
