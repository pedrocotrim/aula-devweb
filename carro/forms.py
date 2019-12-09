from django import forms
from django.core.validators import RegexValidator
from .models import Carro
from desenvolvimentoweb import settings
from datetime import datetime, timedelta


class PesquisaCarroForm(forms.Form):
  class Meta:
      fields = ('busca_por')
  busca_por = forms.CharField(
      widget=forms.TextInput(
          attrs={'class': 'form-control form-control-sm', 'maxlength': '120'}),
      required=False)


class CarroForm(forms.ModelForm):

  class Meta:
      model = Carro
      fields = ('carro_id', 'nome', 'desc', 'marca',
                'preco', 'ano', 'quilometragem')

  carro_id = forms.CharField(widget=forms.HiddenInput(), required=False)

  nome = forms.CharField(
      error_messages={'required': 'Campo obrigatório.'},
      widget=forms.TextInput(
          attrs={'class': 'form-control form-control-sm', 'maxlength': '120'}),
      required=True)

  desc = forms.CharField(
      error_messages={'required': 'Campo obrigatório.', },
      widget=forms.TextInput(
          attrs={'class': 'form-control form-control-sm', 'maxlength': '120'}),
      required=True)

  marca = forms.CharField(
      error_messages={'required': 'Campo obrigatório.'},
      widget=forms.TextInput(
          attrs={'class': 'form-control form-control-sm', 'maxlength': '120'}),
      required=True)

  preco = forms.CharField(
      localize=True,
      error_messages={'required': 'Campo obrigatório.', },
      validators=[RegexValidator(
          regex='^[0-9]{1,7}(,[0-9]{2})?$', message="Informe o valor no formato 9999999,99.")],
      widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                    'maxlength': '20',
                                    'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57) || event.charCode == 44'}),
      required=True)

  ano = forms.IntegerField(
      error_messages={'required': 'Campo obrigatório.'},
      widget=forms.TextInput(
          attrs={'class': 'form-control form-control-sm'}),
      required=True)

  quilometragem = forms.IntegerField(
      error_messages={'required': 'Campo obrigatório.'},
      widget=forms.TextInput(
          attrs={'class': 'form-control form-control-sm'}),
      required=True)

  def clean_preco(self):
      preco = self.cleaned_data.get('preco')

      if not preco:
          return preco

      preco = int(float(preco.replace(',', '.'))*100)

      return preco


class RemoveCarroForm(forms.Form):
  class Meta:
      fields = ('carro_id')
      carro_id = forms.CharField(widget=forms.HiddenInput(), required=True)
