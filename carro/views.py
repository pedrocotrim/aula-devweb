from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'carro/index.html')

def somos(request):
  return render(request,'carro/somos.html')

def carros(request):
  return render(request,'carro/carros.html')

def fale(request):
  return render(request,'carro/fale.html')