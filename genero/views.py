from django.shortcuts import render, redirect,get_object_or_404
from .models import Animacao,Terror,Comedia
import datetime
from django.contrib.auth.decorators import login_required
from .form import animacaoform,terrorform,comediaform


@login_required
def filmes(request):
    data = {}
    data['generoc'] = ['Comédia']
    data['generoa'] = ['Animação']
    data['generot'] = ['Terror']


    data['now'] = datetime.datetime.now()
    return render(request, 'filme.html', data)

@login_required
def list_filmes_comedia(request):
    filmesc= Comedia.objects.all()
    return render(request, 'listfilmecomedia.html',{'filmesc':filmesc})

@login_required
def nova_comedia(request):
    form = comediaform(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('list_filmes_comedia')
    return render(request, 'comediaform.html',{'form':form})

@login_required
def atualizar_comedia(request, id):
    filme= get_object_or_404(Comedia, pk=id)
    form = comediaform(request.POST or None, request.FILES or None, instance=filme)

    if form.is_valid():
        form.save()
        return redirect('list_filmes_comedia')

    return render(request, 'comediaform.html',{'form': form})

@login_required
def deletar_comedia(request,id):
    filme= get_object_or_404(Comedia, pk=id)
    form = comediaform(request.POST or None, request.FILES or None, instance=filme)

    if request.method =='POST':
        filme.delete()
        return redirect('list_filmes_comedia')
    return render(request, 'deletar_form_comedia.html', {'filme':filme})

@login_required
def list_filmes_animacao(request):
    filmesa= Animacao.objects.all()
    return render(request, 'listfilmeanimacao.html', {'filmesa': filmesa})

@login_required
def nova_animacao(request):
    form = animacaoform(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('list_filmes_animacao')
    return render(request, 'animacaoform.html',{'form':form})

@login_required
def atualizar_animacao(request, id):
    filme= get_object_or_404(Animacao, pk=id)
    form = animacaoform(request.POST or None, request.FILES or None, instance=filme)

    if form.is_valid():
        form.save()
        return redirect('list_filmes_animacao')

    return render(request, 'animacaoform.html',{'form': form})

@login_required
def deletar_animacao(request,id):
    filme= get_object_or_404(Animacao, pk=id)
    form = comediaform(request.POST or None, request.FILES or None, instance=filme)

    if request.method =='POST':
        filme.delete()
        return redirect('list_filmes_animacao')
    return render(request, 'deletar_form_animacao.html', {'filme':filme})

@ login_required
def list_filmes_terror(request):
    filmest = Terror.objects.all()
    return render(request, 'listfilmeterror.html', {'filmest': filmest})

@login_required
def nova_terror(request):
    form = terrorform(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('list_filmes_terror')
    return render(request, 'terrorform.html',{'form':form})

@login_required
def atualizar_terror(request, id):
    filme= get_object_or_404(Terror, pk=id)
    form = terrorform(request.POST or None, request.FILES or None, instance=filme)

    if form.is_valid():
        form.save()
        return redirect('list_filmes_terror')

    return render(request, 'terrorform.html',{'form': form})

@login_required
def deletar_terror(request,id):
    filme= get_object_or_404(Terror, pk=id)
    form = comediaform(request.POST or None, request.FILES or None, instance=filme)

    if request.method =='POST':
        filme.delete()
        return redirect('list_filmes_terror')
    return render(request, 'deletar_form_terror.html', {'filme':filme})