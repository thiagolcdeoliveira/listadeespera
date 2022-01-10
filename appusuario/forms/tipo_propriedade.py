# -*- coding: utf-8 -*-
from django.forms import *

from appusuario.models.tipo_propriedade import TipoPropriedade


class TipoPropriedadeAjaxForm(ModelForm):
    class Meta:
        model = TipoPropriedade
        exclude = ('usuario', 'excluido', 'desativado')


class TipoPropriedadeForm(ModelForm):
    class Meta:
        model = TipoPropriedade
        exclude = ('usuario', 'excluido', 'desativado')
