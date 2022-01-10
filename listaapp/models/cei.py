# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.db.models import SET_NULL
from django.urls import reverse

from ..models.secretaria import Secretaria


class Cei(models.Model):
    '''
    :param nome: models.CharField(max_length=200, verbose_name="Extensão",
                                help_text='Tipo de arquivo (Exemplo: PDF, DOC ou DOCX).')
    :param usuario: models.ForeignKey(User, verbose_name="Usuário")
    :param excluido: models.BooleanField(default=False, verbose_name="Excluído")
    :param desativado: models.BooleanField(default=False)
    '''
    nome = models.CharField(max_length=200, verbose_name="Nome do Setor",
                                help_text='Nome do Setor (Exemplo: TI, Compras , etc .).')
    servidor = models.ForeignKey(User,  related_name="servidor_usuario_setor", verbose_name="Servidor Responsavel",on_delete=SET_NULL, null=True)
    secretaria = models.ForeignKey(Secretaria,blank=True, verbose_name="Setor Superior",on_delete=SET_NULL, null=True)
    usuario = models.ForeignKey(User, verbose_name="Usuário",on_delete=SET_NULL, null=True)
    excluido = models.BooleanField(default=False, verbose_name="Excluído")
    desativado = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.nome

    def __str__(self):
        return u'%s' % self.nome

    def get_absolute_url(self):
        return reverse('setor-detail', kwargs={'pk': self.pk})

    class Meta:
        app_label = "listaapp"
        verbose_name = 'Cei'
        verbose_name_plural = 'Ceis'
        permissions = (
            ("lisapp_add_cei", "Adicionar Cei"),
            ("listaapp_detail_cei", "Visualizar Cei"),
            ("listaapp_delete_cei", "Excluir Cei"),
        )
