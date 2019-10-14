from django.db import models

# Create your models here.

class Vendedor(models.Model):
  nome = models.CharField(max_length=64)
  email = models.CharField(max_length=64)
  cidade = models.CharField(max_length=64)

  def __str__(self):
    return self.nome

class Carro(models.Model):
  nome = models.CharField(max_length=64)
  slug = models.SlugField(max_length=200)
  desc = models.TextField()
  vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
  preco = models.IntegerField()
  ano = models.IntegerField()
  quilometragem = models.DecimalField(decimal_places=2, max_digits=5)

  def __str__(self):
    return "{} {}".format(self.nome,self.ano)

class Imagem(models.Model):
  caminho = models.CharField(max_length=50)
  pagina = models.CharField(max_length=50)

class Text(models.Model):
  texto = models.TextField()
  pagina = models.CharField(max_length=50)