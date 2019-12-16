from django.urls import path
from . import views

app_name= 'carro'

urlpatterns = [
    path('', views.index, name='index'),
    path('quem-somos/', views.somos, name='somos'),
    path('fale-conosco/', views.fale, name='fale'),
    path('carros/', views.lista_carro, name='lista_carro'),
    path('cadastra_carro/', views.cadastra_carro, name='cadastra_carro'),
    path('exibe_carro/<int:id>/', views.exibe_carro, name='exibe_carro'),
    path('edita_carro/<int:id>/', views.edita_carro, name='edita_carro'),
    path('remove_carro/', views.remove_carro, name='remove_carro'),
    path('pesquisa_carro/', views.pesquisa_carro, name='pesquisa_carro'),
    path('adicionar_ao_carrinho/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('remove_carro_carrinho/', views.remove_carro_carrinho, name='remove_carro_carrinho'),
    path('atualiza_qtd_carrinho/', views.atualiza_qtd_carrinho, name='atualiza_qtd_carrinho'),
    path('exibe_carrinho/', views.exibe_carrinho, name='exibe_carrinho'),
]
