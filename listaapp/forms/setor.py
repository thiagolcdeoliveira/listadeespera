# -*- coding: utf-8 -*-

from django.forms import *
from listaapp.models.cei import Cei


class CeiAjaxForm(ModelForm):

    class Meta:
        model = Cei
        exclude = ('usuario', 'excluido', 'desativado')