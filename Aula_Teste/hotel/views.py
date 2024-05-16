from django.shortcuts import render,HttpResponse
from .models import hotel, quarto, reserva
from .forms import FormReserva

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

def reservas(request):
    context = {}
    dados_hotel = hotel.objects.all()
    context["dados_hotel"] = dados_hotel
    dados_quarto = quarto.objects.all()
    context["dados_quarto"] = dados_quarto

    # Se a minha requisição for do método POST
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = FormReserva(request.POST)
        # Validando se é valido
        if form.is_valid():
            # Salvando os dados inseridos no forms
            # Criar uma variavel para armazenar os dados
            var_nome = form.cleaned_data['nome']
            var_sobrenome = form.cleaned_data['sobrenome']
            var_email = form.cleaned_data['email']
            var_idade = form.cleaned_data['idade']
            var_endereco = form.cleaned_data['endereco']
            var_quarto = form.cleaned_data['quarto']
            var_data = form.cleaned_data['data']

            user = reserva(nome=var_nome, sobrenome=var_sobrenome, email=var_email, idade=var_idade, endereco = var_endereco, quarto=var_quarto, data=var_data)
            user.save()

            return HttpResponse("<h1>thanks</h1>")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FormReserva()
    
        context['form'] = form

        # Vou redenrizar o que foi criado no arquivo forms
        return render(request, "reserva.html", context)