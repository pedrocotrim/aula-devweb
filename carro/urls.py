from django.urls import path
from . import views

app_name= 'carro'

urlpatterns = [
    path('', views.index, name='index'),
    path('quem-somos/', views.somos, name='somos'),
    path('fale-conosco/', views.fale, name='fale'),
    path('carros/', views.carros, name='carros')
]
