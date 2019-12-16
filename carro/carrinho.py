from decimal import Decimal
from desenvolvimentoweb import settings

from .models import Carro

class Carrinho(object):

    def __init__(self, request):
        self.session = request.session

        self.carrinho = self.session.get(settings.CARRINHO_SESSION_ID)
        if not self.carrinho:
            self.carrinho = self.session[settings.CARRINHO_SESSION_ID] = {}

    def __len__(self):
        """ Conta todos os itens no carrinho. """
        return sum(item['quantidade'] for item in self.carrinho.values())

    def get_carros(self):
        lista = []
        for item in self.carrinho.values():
            carro = Carro.objects.get(id=item['id'])
            lista.append({'carro': carro,
                          'preco': item['preco'],
                          'quantidade': item['quantidade']})
        return lista

    def adicionar(self, id, quantidade):
        carro = Carro.objects.get(id=id)

        if id not in self.carrinho:
            self.carrinho[id] = {'id': id, 'preco': str(carro.preco), 'quantidade': quantidade}
        else:
            self.carrinho[id]['quantidade'] += quantidade
        self.salvar()

    def alterar(self, id, quantidade):       
        self.carrinho[id]['quantidade'] = quantidade
        self.salvar()

    def remover(self, id):
        if id in self.carrinho:
            del self.carrinho[id]
            self.salvar()

    def salvar(self):
        self.session.modified = True

    def limpar(self):
        self.session[settings.CARRINHO_SESSION_ID] = {}

    def get_preco_total(self):
        return "{:.2f}".format(sum(int(item['preco'])/100 * item['quantidade'] for item in self.carrinho.values())).replace('.',',')
