import datetime
from tkinter import ALL, N
from django.db import models
from accounts.models import Usuario
from django.core.validators import MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField
# Create your models here.   


class Redacao(models.Model):
    #area como um campo de multipla escolha
    AREA_CHOICES = (
        ("C",   "Ciencias"),
        ("B",   "Biologia"),
        ("S",   "Sociedade"),
        ("E",   "Engenharias"),
        ("L",   "Linguística"),        
        ("P",   "Política"),
        ("H",   "História"),
    )
    
    
    titulo = models.CharField(
        max_length = 45, 
        blank = False,
        null = False,
    )

    area = MultiSelectField(
        max_length=20, 
        max_choices=4,
        choices= AREA_CHOICES,
        blank=False, 
        null = False,
    )

    tema = models.CharField(
        blank=False, 
        null = False,
        max_length=45
    )
    #instancio a data de criação no momento em que o objeto é criado

    conteudo = models.TextField(
        blank = False,
        null = False,
        max_length= 15000
    )
    
    #comentário
    descricao = models.TextField(
        max_length=300, 
        blank= True,
        null= True,
        default=None
    )

    data_criacao = models.DateTimeField(
        default=datetime.date.today
    )
   
    #Relaciono redação com a classe Usuario - 1 - N = " 1 Usuario escreve N redações"
    fk_autor = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='Redacao'
    )
    
    #Relaciono redação com a classe Usuario - N - N = "N  Usuarios escrevem N redações" 
    avaliacoes = models.ManyToManyField(
        Usuario, 
        related_name="redacoesAvaliadas",
        through="Avaliacao"
    )
    
    def __str__(self):
        return "Autor: {} | Titulo: {} | Area: {} | Tema: {} | Data: {}\n".format(self.fk_autor.username, self.titulo, self.area, self.tema, self.data_criacao)


class Avaliacao(models.Model):
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='Usuario_avaliacao'
    )
    redacao = models.ForeignKey(
        Redacao,
        on_delete=models.CASCADE,
        related_name='Usuario_avaliacao'
    )
    comentario = models.TextField(
        max_length=300, 
        blank = False,
        null = False,
    )

    nota = models.SmallIntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ],
        blank = False,
        null = False,
    )

    data_criacao = models.DateTimeField(
        default=datetime.date.today
    )
    def __str__(self):
        return "Avaliador: {} - Redação Avaliada: {} - Nota dada: {}\n".format(self.usuario.username, self.redacao.titulo, self.nota)


class Filtro(models.Model):
    #area como um campo de multipla escolha
    AREA_CHOICES = (
        ("C",   "Ciencias"),
        ("B",   "Biologia"),
        ("S",   "Sociedade"),
        ("E",   "Engenharias"),
        ("L",   "Linguística"),        
        ("P",   "Política"),
        ("P",   "História"),
    )
    # AVALIADA_CHOICES = (
    #     ('S', "Sim"),
    #     ('N', "Não"),
    # )
    titulo = models.CharField(
        max_length = 45, 
        blank = True,
        null = True,
        
    )
    autor = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='Filtros',
        blank = True,
        null = True,
    )
    tema = models.CharField(
        blank = True,
        null = True,
        max_length=45,
        default= 'All'
    )

    # avaliada = models.CharField(
    #     max_length=1, 
    #     choices= AVALIADA_CHOICES,
    #     blank = True,
    #     null = True,
    #     default = 'N',
    # )
   
    area = MultiSelectField(
        max_length=40, 
        max_choices=10,
        choices= AREA_CHOICES,
        blank = True,
        null = True,
        default =  ["CET", "CB", "CSA", "E", "LLA", "CH",]
    )

    
   



# class Comentario:

