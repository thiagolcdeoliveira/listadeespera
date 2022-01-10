# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.db.models import SET_NULL
from django.urls import reverse


class Turma(models.Model):
    '''
    :param nome: models.CharField(max_length=200, verbose_name="Extensão",
                                help_text='Tipo de arquivo (Exemplo: PDF, DOC ou DOCX).')
    :param usuario: models.ForeignKey(User, verbose_name="Usuário")
    :param excluido: models.BooleanField(default=False, verbose_name="Excluído")
    :param desativado: models.BooleanField(default=False)
    '''
    nome = models.CharField(max_length=200, verbose_name="Nome da Secretaria",
                                help_text='Nome da Secretaria (Exemplo: Administraçao, Governo, etc .).')
    responsavel = models.ForeignKey(User, related_name="responsavel_usuario_turma", verbose_name="Servidor Responsavel",on_delete=SET_NULL, null=True)
    usuario = models.ForeignKey(User, verbose_name="Usuário",on_delete=SET_NULL, null=True)

    excluido = models.BooleanField(default=False, verbose_name="Excluído")
    desativado = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.nome

    def __str__(self):
        return u'%s' % self.nome
    def get_absolute_url(self):
        return reverse('secretaria-detail', kwargs={'pk': self.pk})

    class Meta:
        app_label = "listaapp"
        verbose_name = 'listaapp'
        verbose_name_plural = 'Turmas'
        permissions = (
            ("baseapp_add_turma", "Adicionar Secretaria"),
            ("baseapp_detail_turma", "Visualizar Secretaria"),
            ("baseapp_delete_turma", "Excluir Secretaria"),
        )
