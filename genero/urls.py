from django.urls import path
from .views import list_filmes, filmes,nova_comedia,nova_animacao,nova_terror
from .views import atualizar_comedia, deletar_comedia,atualizar_animacao, deletar_animacao,atualizar_terror, deletar_terror

urlpatterns = [
    path('filmes/', filmes, name='filmes'),
    path('listfilme/', list_filmes, name='list_filmes'),
    path('comedia/', nova_comedia, name='nova_comedia'),
    path('animacao/', nova_animacao, name='nova_animacao'),
    path('terror/', nova_terror, name='nova_terror'),
    path('atualizar/<int:id>/', atualizar_comedia, name='atualizar_comedia'),
    path('deletar/<int:id>/', deletar_comedia, name='deletar_comedia'),
    path('atualizar/<int:id>/', atualizar_animacao, name='atualizar_animacao'),
    path('deletar/<int:id>/', deletar_animacao, name='deletar_animacao'),
    path('atualizar/<int:id>/', atualizar_terror, name='atualizar_terror'),
    path('deletar/<int:id>/', deletar_terror, name='deletar_terror'),
]