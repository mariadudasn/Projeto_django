from django.shortcuts import render,HttpResponse
from .models import hotel
from .models import quarto

# Create your views here.
def homepage(request):
    #Criei um dicionário
    context = {}
    #Criei uma variável e atribui a essa variavel a consulta do banco
    dados_hotel = hotel.objects.all()
    #Chave é o que o html irá conseguir movimentar
    #Por padrão o nome da lista é o nome da chave
    context["dados_hotel"] = dados_hotel
    return render(request,'homepage.html', context)


def quartos(request):
    context = {}
    dados_hotel = hotel.objects.all()
    context["dados_hotel"] = dados_hotel
    dados_quarto = quarto.objects.all()
    context["dados_quarto"] = dados_quarto
    return render(request,'quartos.html', context)