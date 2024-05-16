from django import forms

TIPOS_QUARTOS = (
    ("SOLTEIRO", "Solteiro"),
    ("CASAL", "Casal"),
    ("CONFORTO", "Conforto"),
    ("LUXO", "Luxo")
)

class FormReserva (forms.Form):
    nome = forms.CharField(label='Nome:', max_length=20)
    sobrenome = forms.CharField(label='Sobrenome:', max_length=50)
    email = forms.CharField(label='Email:', max_length=50)
    idade = forms.IntegerField(label='Idade:', min_value=0)
    endereco = forms.CharField(label='Endereço:', max_length=50)
    quarto = forms.ChoiceField(label='Quarto:', choices=TIPOS_QUARTOS)
    data = forms.DateTimeField(label="Data", widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))


