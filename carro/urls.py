from django.urls import path
from . import views

app_name= 'carro'

urlpatterns = [
    path('', views.index, name='index'),
    path('quem-somos/', views.somos, name='somos'),
    path('fale-conosco/', views.fale, name='fale'),
    path('carro/carros/', views.lista_carro, name='lista_carro'),
    path('carro/cadastra_carro/', views.cadastra_carro, name='cadastra_carro'),
    path('carro/exibe_carro/<int:id>/', views.exibe_carro, name='exibe_carro'),
    path('carro/edita_carro/<int:id>/', views.edita_carro, name='edita_carro'),
    path('carro/remove_carro/', views.remove_carro, name='remove_carro'),
    path('carro/pesquisa_carro/', views.pesquisa_carro, name='pesquisa_carro'),
]
