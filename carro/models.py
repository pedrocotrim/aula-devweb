from django.db import models

# Create your models here.

class Carro(models.Model):
  nome = models.CharField(max_length=64)
  slug = models.SlugField(max_length=200)
  desc = models.TextField()
  marca = models.CharField(max_length=64)
  preco = models.IntegerField()
  ano = models.IntegerField()
  quilometragem = models.IntegerField()

  def __str__(self):
    return "{} {}".format(self.nome,self.ano)

class Imagem(models.Model):
  caminho = models.CharField(max_length=50)
  pagina = models.CharField(max_length=50)

class Text(models.Model):
  texto = models.TextField()
  pagina = models.CharField(max_length=50)