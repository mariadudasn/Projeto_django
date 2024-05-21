from django.shortcuts import render,HttpResponse, redirect
from .models import hotel, quarto, reserva
from .forms import FormReserva
from .forms import FormCadastro
from django.contrib.auth.models import User
from .forms import FormLogin
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

# Create your views here.
def homepage(request):
    #Criei um dicionário
    context = {}
    #Criei uma variável e atribui a essa variavel a consulta do banco
    dados_hotel = hotel.objects.all()
    #Chave é o que o html irá conseguir movimentar
    #Por padrão o nome da lista é o nome da chave
    context["dados_hotel"] = dados_hotel
    if request.user.is_authenticated:
        return render(request,'homepage2.html', context)
    else:
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

            response_html = """
                <html>
                    <head>
                        <title>Reserva Feita</title>
                        <style>
                            .back-button {
                                display: inline-block;
                                padding: 10px 20px;
                                font-size: 16px;
                                color: #000;
                                background-color: #f3dbc36c;
                                border: 2px solid #f3dbc36c;
                                text-decoration: none;
                                border-radius: 5px;
                                transition: background-color 0.3s, color 0.3s;
                            }

                            .back-button:hover {
                                background-color: #eaccadc0;
                                color: #fff;
                            }

                            .container {
                                text-align: center;
                                padding: 50px;
                            }
                        </style>
                    </head>
                    <body>
                        <div class="container">
                            <h1>Sua reserva foi feita!</h1>
                            <a href="/quartos" class="back-button">Voltar</a>
                        </div>
                    </body>
                </html>
                """
            return HttpResponse(response_html)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FormReserva()
    
        context['form'] = form

        # Vou redenrizar o que foi criado no arquivo forms
        return render(request, "reserva.html", context)
    
def cadastro(request):
    context = {}
    dados_hotel = hotel.objects.all()
    context["dados_hotel"] = dados_hotel
    dados_quarto = quarto.objects.all()
    context["dados_quarto"] = dados_quarto
    if request.method == "POST":
        form = FormCadastro(request.POST)
        if form.is_valid():
            var_first_name = form.cleaned_data['first_name']
            var_last_name = form.cleaned_data['last_name']
            var_user = form.cleaned_data['user']
            var_email = form.cleaned_data['email']
            var_password = form.cleaned_data['password']

            user = User.objects.create_user(username=var_user, email=var_email, password=var_password)
            user.first_name=var_first_name
            user.last_name=var_last_name
            user.save()

            return HttpResponse("<h1>Deu certo</h1>")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FormCadastro()

        context['form'] = form

        # Vou redenrizar o que foi criado no arquivo forms
        return render(request, "cadastro.html", context)

def login(request):
    context = {}
    dados_hotel = hotel.objects.all()
    context["dados_hotel"] = dados_hotel
    dados_quarto = quarto.objects.all()
    context["dados_quarto"] = dados_quarto
    if request.method == "POST":
        form = FormLogin(request.POST)
        if form.is_valid():
            var_user = form.cleaned_data['user']
            var_password = form.cleaned_data['password']

            user = authenticate(username=var_user, password=var_password)
            if user is not None:
                auth_login(request, user)
                return redirect('quartos')
            else:
                return HttpResponse("<h1>Login Invalido</h1>")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FormLogin()

        context['form'] = form

        # Vou redenrizar o que foi criado no arquivo forms
        return render(request, "login.html", context)