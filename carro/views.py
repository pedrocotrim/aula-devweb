from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .forms import CarroForm, RemoveCarroForm, PesquisaCarroForm, QuantidadeForm, RemoveCarroDoCarrinhoForm
from .models import Imagem, Text, Carro
from carro.carrinho import Carrinho

# Create your views here.

def index(request):
    imagens = get_list_or_404(Imagem, pagina='index')
    html = get_list_or_404(Text, pagina='index')
    return render(request, 'carro/index.html', {'imagens': imagens, 'text': html})

def somos(request):
    html = get_list_or_404(Text, pagina='somos')
    return render(request, 'carro/somos.html', {'text': html})

def fale(request):
    return render(request, 'carro/fale.html')


def pesquisa_carro(request):
    form = PesquisaCarroForm()
    return render(request, 'carro/pesquisa_carro.html', {
        'form': form
    })

def lista_carro(request):
    form = PesquisaCarroForm(request.GET)
    if (form.is_valid()):
        busca_por = form.cleaned_data['busca_por']
        lista_de_carros = Carro.objects.filter(
            nome__icontains=busca_por).order_by('nome')
        items_por_pagina = request.GET.get('numItens')
        if not items_por_pagina:
            items_por_pagina = 5
        paginator = Paginator(lista_de_carros, items_por_pagina)
        pagina = request.GET.get('pagina')
        carros = paginator.get_page(pagina)

        lista_de_ids = []
        for carro in carros:
            carro.preco = "{:.2f}".format(carro.preco/100).replace('.', ',')
            lista_de_ids.append(carro.id)

        return render(request, 'carro/pesquisa_carro.html', {
            'form': form,
            'carros': carros,
            'lista_de_ids': lista_de_ids
        })

    else:
        raise ValueError(
            'Ocorreu um erro inesperado ao tentar pesquisar um carro.')


def cadastra_carro(request):
    if request.POST:
        carro_id = request.POST.get('carro_id')
        if carro_id:
            carro = get_object_or_404(Carro, pk=carro_id)
            carro_form = CarroForm(request.POST, instance=carro)
        else:
            carro_form = CarroForm(request.POST)

        if carro_form.is_valid():
            carro = carro_form.save()
            if carro_id:
                messages.add_message(request, messages.INFO,
                                     'Carro alterado com sucesso!')
            else:
                messages.add_message(request, messages.INFO,
                                     'Carro cadastrado com sucesso!')
            return redirect('carro:exibe_carro', id=carro.id)
        else:
            messages.add_message(request, messages.ERROR,
                                 'Corrija o(s) erro(s) abaixo.')
    else:
        carro_form = CarroForm()
    return render(request, 'carro/cadastra_carro.html', {
        'form': carro_form
    })


def exibe_carro(request, id):
    carro = get_object_or_404(Carro, pk=id)
    form_remove_carro = RemoveCarroForm()
    form_remove_carro.fields['carro_id'].initial = id
    form_adiciona_carrinho = QuantidadeForm()
    form_adiciona_carrinho.fields['quantidade'].initial = 1
    form_adiciona_carrinho.fields['carro_id'].initial = id
    return render(request, 'carro/exibe_carro.html', {
        'carro': carro,
        'form_remove_carro': form_remove_carro,
        'form': form_adiciona_carrinho
    })


def edita_carro(request, id):
    carro = get_object_or_404(Carro, pk=id)
    carro_form = CarroForm(instance=carro)
    carro_form.fields['carro_id'].initial = id

    return render(request, 'carro/cadastra_carro.html', {
        'form': carro_form
    })


def remove_carro(request):
    carro_id = request.POST.get('carro_id')
    carro = get_object_or_404(Carro, id=carro_id)
    carro.delete()
    messages.add_message(request, messages.INFO, 'Carro removido com sucesso.')
    return render(request, 'carro/exibe_carro.html', {'carro': carro})


def adicionar_ao_carrinho(request):
    form = QuantidadeForm(request.POST)
    if form.is_valid():
        quantidade = form.cleaned_data['quantidade']
        carro_id = form.cleaned_data['carro_id']

        carrinho = Carrinho(request)
        carrinho.adicionar(carro_id, quantidade)

        return exibe_carrinho(request)
    else:
        print(form.errors)
        raise ValueError(
            'Ocorreu um erro inesperado ao adicionar um carro ao carrinho.')


def remove_carro_carrinho(request):
    form = RemoveCarroDoCarrinhoForm(request.POST)
    if form.is_valid():
        carrinho = Carrinho(request)
        carrinho.remover(form.cleaned_data['carro_id'])

        return exibe_carrinho(request)
    else:
        print(form.errors)
        raise ValueError(
            'Ocorreu um erro inesperado ao adicionar um carro ao carrinho.')


def atualiza_qtd_carrinho(request):
    form = QuantidadeForm(request.POST)
    if form.is_valid():
        carro_id = form.cleaned_data['carro_id']
        quantidade = form.cleaned_data['quantidade']

        carrinho = Carrinho(request)
        carrinho.alterar(carro_id, quantidade)

        return exibe_carrinho(request)
    else:
        print(form.errors)
        raise ValueError(
            'Ocorreu um erro inesperado ao adicionar um carro ao carrinho.')


def exibe_carrinho(request):
  carrinho = Carrinho(request)
  lista_de_carros_no_carrinho = carrinho.get_carros()
  carros_no_carrinho = []
  lista_de_forms = []
  lista_de_ids = []
  valor_do_carrinho = 0
  for item in lista_de_carros_no_carrinho:
      carros_no_carrinho.append(item['carro'])
      lista_de_forms.append(QuantidadeForm(
          initial={'quantidade': item['quantidade']}))
      valor_do_carrinho = carrinho.get_preco_total()

  for carro in carros_no_carrinho:
      carro.preco = "{:.2f}".format(carro.preco/100).replace('.', ',')
  return render(request, 'carro/exibe_carrinho.html',  {
      'listas': zip(carros_no_carrinho, lista_de_forms),
      'valor_do_carrinho': valor_do_carrinho,
  })
