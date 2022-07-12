
from RedifApp import views
from RedifApp.models import Redacao
from accounts.models import Usuario

# def filtrar(request):
#     titulo = request.GET.get('titulo')
#     area = request.GET.get('area')
#     tema = request.GET.get('tema')
#     autor = request.GET.get('autor')

#     redacoes = Redacao.objects.all()

#     if titulo: redacoes.filter(titulo__icontains = titulo) 
#     if area: redacoes.filter(area__icontains = area) 
#     if tema: redacoes.filter(tema__icontains = tema) 
#     if autor: redacoes.filter(autor__icontains = autor) 

#     return redacoes

def filtrar(form):
    redacoes = Redacao.objects.all()
    if not form.is_valid(): return redacoes
    
   
    titulo = form.cleaned_data['titulo']
    area = form.cleaned_data['area']
    tema = form.cleaned_data['tema']
    autor = form.cleaned_data['autor']
    perfil = Usuario.objects.filter(username = autor)
    # avaliada = form.cleaned_data['avaliada']

    # if avaliada:
    #     if avaliada == 'S':
    #         redacoes = Redacao.objects.filter(Redacao.Usuario_avaliacao.exists())

    if titulo: 
        redacoes = redacoes.filter(titulo__icontains = titulo)    
    if tema: 
        redacoes = redacoes.filter(tema__icontains = tema) 
    if autor:        
        redacoes = redacoes.filter(fk_autor = perfil[0])
       
    if not area: return redacoes
    else:  return filtrarArea(redacoes, area)


def filtrarArea(redacoes, areas):
    lista = []
    for item in list(redacoes):
        for x in list(item.area):
            if x in list(areas): 
                lista.append(item)
    return lista
