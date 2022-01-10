# -*- coding: utf-8 -*-

from django.forms import *

from appusuario.models.endereco import Endereco


class EnderecoAjaxForm(ModelForm):

    class Meta:
        model = Endereco
        exclude = ('usuario', 'excluido', 'desativado')