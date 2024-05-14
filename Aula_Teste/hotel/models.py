from django.db import models

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
    descricao = models.TextField(max_length=500)
    logo = models.ImageField(upload_to="logo/")

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