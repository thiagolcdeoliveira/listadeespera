# -*- coding: utf-8 -*-
import hashlib

from django.contrib.auth.models import User
from django.db import models
from django.db.models import SET_NULL
from django.urls import reverse

from baseapp.models.imagem import Imagem
from baseapp.models.mensagem import Mensagem

from appusuario.models.propriedade import Propriedade
from .turma import Turma

from ..models.produto import Produto
from ..models.equipamento import Equipamento
from ..models.prioridade import Prioridade
from ..models.cei  import Cei
from ..models.situacao import Situacao
from ..models.tipo_chamado import TipoChamado
from ..views.crianca.caclulo import calculoTurma

Turmas = (
    (1, "Bercario 1"),
    (2, "Bercario 2"),
    (3, "Maternal"),
    (4, "Jardim"),
    (5, "Pré"),
    (6, "FIC"),
)

class Crianca(models.Model):
    '''
    :param nome: models.CharField(max_length=200, verbose_name="Extensão",
                                help_text='Tipo de arquivo (Exemplo: PDF, DOC ou DOCX).')
    :param usuario: models.ForeignKey(User, verbose_name="Usuário")
    :param excluido: models.BooleanField(default=False, verbose_name="Excluído")
    :param desativado: models.BooleanField(default=False)
    '''
    codigo = models.CharField(max_length=200, verbose_name="Codigo da Criança",blank=True)
    nome = models.CharField(max_length=200, verbose_name="Nome")
    sobrenome = models.CharField(max_length=200, verbose_name="Sobrenomenome")
    cpf = models.CharField(max_length=200, verbose_name="CPF")

    # tipo_chamado = models.ForeignKey(TipoChamado, verbose_name="Tipo Chamado",on_delete=SET_NULL, null=True)
    # prioridade = models.ForeignKey(Prioridade, verbose_name="Prioridade",on_delete=SET_NULL, null=True)
    usuario = models.ForeignKey(User, verbose_name="Usuário",on_delete=SET_NULL, null=True)
    responsavel = models.ForeignKey(User, verbose_name="Responsavel",
                                    help_text='Servidor responsavel data TI pelo chamado .',
                                    related_name='responsavel_usuario', on_delete=SET_NULL, null=True)


    cei = models.ManyToManyField(Cei, verbose_name="Cei",
                                    help_text='Cei desejado .',
                                     null=True)
    # on_delete = SET_NULL,

    data_cadastro = models.DateTimeField(auto_now_add=True, null=True)
    data_nasc = models.DateField(blank=True,null=False)
    data_retirada_fila = models.DateTimeField(blank=True, null=True)
    #turma = models.CharField(max_length=1, choices=Turmas, blank=True, null=True)
    turma = models.ForeignKey(Turma, verbose_name="Turma",
                                   help_text='Turma definida .',
                                   on_delete=SET_NULL, null=True, blank=True)
    situacao = models.ForeignKey(Situacao,on_delete=SET_NULL, null=True,blank=True)
    autorizacao = models.BooleanField(default=False, verbose_name="Excluído")
    excluido = models.BooleanField(default=False, verbose_name="Excluído")
    desativado = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.cod

    def __str__(self):
        return u'%s' % self.nome

    def get_absolute_url(self):
        return reverse('crianca-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if not self.codigo:
            hash_codigo = (hash(str(self.id)))
            self.codigo =  u'#%s' % ( hash_codigo if hash_codigo  >= 0 else hash_codigo*-1 )
        #if not self.turma:
       # self.turma = calculoTurma(self.data_nasc)
        self.turma ,created = Turma.objects.get_or_create(id=calculoTurma(self.data_nasc))
        super(Crianca, self).save(*args, **kwargs)

    class Meta:
        app_label = "listaapp"
        verbose_name = 'Criança'
        verbose_name_plural = 'Crianças'
        permissions = (
            ("listaapp_add_crianca", "Adicionar Crianca"),
            ("listaapp_detail_crianca", "Visualizar Crianca"),
            ("listaapp_delete_crianca", "Excluir Crianca"),
            ("listaapp_list_crianca", "Listar Crianca"),
        )
