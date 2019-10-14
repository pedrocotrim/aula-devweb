from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Imagem, Text

# Create your views here.
def index(request):
  imagens = get_list_or_404(Imagem, pagina='index')
  html = get_list_or_404(Text, pagina='index')
  return render(request, 'carro/index.html', { 'imagens': imagens, 'text': html })

def somos(request):
  html = get_list_or_404(Text, pagina='somos')
  return render(request,'carro/somos.html', { 'text': html })

def carros(request):
  return render(request,'carro/carros.html')

def fale(request):
  return render(request,'carro/fale.html')