from django.db import models
from django.utils import timezone

# Create your models here.

#Tupla
TIPOS_QUARTOS = (
    # O que está maiúsculo aparecerá no banco
    # Em minúsculo -> vai aparecer na hora de cadastrar
    ("SOLTEIRO", "Solteiro"),
    ("CASAL", "Casal"),
    ("CONFORTO", "Conforto"),
    ("LUXO", "Luxo")
)

# Homepage
class hotel (models.Model):
    # CharField -> texto curto
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=1800)
    logo = models.ImageField(upload_to="logo/")
    hotel = models.ImageField(upload_to="foto_hotel/")

    def __str__(self):
        return self.titulo

# Não montar nada no plural
class quarto(models.Model):
    # Choices (documentação)
    # Os tipos, já são pré-definidos -> lista de tuplas -> não podem ser alterados
    tipo = models.CharField(max_length=15, choices=TIPOS_QUARTOS)
    disponibilidade = models.IntegerField()
    valor = models.FloatField(max_length=4)
    descricao = models.TextField(max_length=255)
    foto_quarto = models.ImageField(upload_to="foto_quarto/")

    def __str__(self):
        return self.tipo
    
class reserva(models.Model):
    nome = models.CharField(max_length=25)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    idade = models.IntegerField()
    endereco = models.CharField(max_length=50)
    quarto = models.CharField(max_length=50, choices=TIPOS_QUARTOS)
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome