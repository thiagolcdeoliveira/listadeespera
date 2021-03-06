# coding=utf-8
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from django.views.generic import *

from baseapp.forms.noticacao import NotificacaoForm
from baseapp.models.notificacao import Notificacao

from baseapp.variaveis import *


class NotificacaoListView(PermissionRequiredMixin, ListView):
    permission_required = ADD_CHAMADO
    template_name = 'notificacao/notificacao_list.html'
    model = Notificacao
    queryset = Notificacao
    paginate_by = 10
    form_class = NotificacaoForm
    select = {'todos': '0', 'codigo': '1', 'nome': '2', 'solicitante': '3', 'responsavel': '4',
              'descricao': '5'
              }

    def get_queryset(self):

         form = self.request.GET
         self.queryset = Notificacao.objects.all()
         descricao = form.get('descricao')
         query = get_queryset_filter(self,form,descricao)
         return query.order_by('status','-id').reverse()


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['select'] = self.select
        context['form'] = self.form_class
        return context


def get_queryset_filter(self,form,descricao):

     if form.get('tipo'):

         if form.get('tipo') == self.select.get("descricao"):
            self.queryset = self.queryset.filter(descricao__icontains=descricao)
         elif form.get('tipo') == self.select.get("servidor"):
             self.queryset = self.queryset.filter(Q(solicitante__username__icontains=descricao) |
             Q(solicitante__first_name__icontains=descricao) | Q(solicitante__last_name__icontains=descricao))
         elif form.get('tipo') == self.select.get("codigo"):
             if descricao.isdigit():
                self.queryset = self.queryset.filter(pk=form.get('descricao'))
         elif form.get('tipo') == self.select.get("responsavel"):
             print(descricao)
             self.queryset = self.queryset.filter(responsavel__username__icontains=descricao)
         elif form.get('tipo') == self.select.get("nome"):
             self.queryset = self.queryset.filter(nome__icontains=descricao)
         elif form.get('tipo') == '0':
             if descricao.isdigit():
                 self.queryset = self.queryset.filter(
                     Q(descricao__icontains=descricao) | Q(solicitante__username__icontains=descricao)
                     | Q(pk=descricao) | Q(nome__icontains=descricao) | Q(responsavel__username__icontains=descricao)
                     |Q(solicitante__username__icontains=descricao) | Q(solicitante__first_name__icontains=descricao)
                     | Q(solicitante__last_name__icontains=descricao)
                 )
             else:
                 self.queryset = self.queryset.filter(
                     Q(descricao__icontains=descricao) | Q(solicitante__username__icontains=descricao)
                     |  Q(nome__icontains=descricao) | Q(responsavel__username__icontains=descricao)|
                     Q(solicitante__first_name__icontains=descricao)   | Q(solicitante__last_name__icontains=descricao)
                 )
     if form.get('status')=='1':
         self.queryset = self.queryset.filter(status=False)
     elif form.get('status')=='2':
         self.queryset = self.queryset.filter(status=True)
     if form.get('data_incio'):
         self.queryset = self.queryset.filter(data_inicio__gte=form.get('data_incio'))
     if form.get('data_fim'):
         self.queryset = self.queryset.filter(data_inicio__lte=form.get('data_fim'))
     if form.get('data_incio_encerramento'):
         self.queryset = self.queryset.filter(data_fim__gte=form.get('data_incio_encerramento'))
     if form.get('data_fim_encerramento'):
         self.queryset = self.queryset.filter(data_fim__lte=form.get('data_fim_encerramento'))
     if form.get('setor'):
         self.queryset = self.queryset.filter(setor=form.get('setor'))
     # if form.get('tipo'):
     # return self
     return self.queryset.filter(excluido=False).order_by('id').reverse()


class NotificacaoPorResposavelListView(PermissionRequiredMixin, ListView):
    permission_required = ADD_CHAMADO
    template_name = 'notificacao/notificacao_list.html'
    model = Notificacao
    queryset = Notificacao
    paginate_by = 10
    form_class = NotificacaoForm
    select = {'todos': '0', 'codigo': '1', 'nome': '2', 'solicitante': '3', 'responsavel': '4',
              'descricao': '5'
              }

    def get_queryset(self):

         form = self.request.GET
         # self.queryset = Chamado.objects.all()

         self.queryset = Notificacao.objects.filter(responsavel=self.request.user)
         descricao = form.get('descricao')
         query = get_queryset_filter(self, form, descricao)
         return query


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['select'] = self.select
        context['form'] = self.form_class

        return context

# class TipoArquivoCreateView(PermissionRequiredMixin, CreateView):
class NotificacaoMeuListView(ListView):
    # permission_required = ADD_CHAMADO
    template_name = 'notificacao/notificacao_list.html'
    model = Notificacao
    queryset = Notificacao
    paginate_by = 10
    form_class = NotificacaoForm
    select = {'todos': '0', 'codigo': '1', 'nome': '2', 'solicitante': '3', 'responsavel': '4',
              'descricao': '5'
              }

    def get_queryset(self):

         form = self.request.GET
         self.queryset = Notificacao.objects.filter(usuario_recebe=self.request.user, excluido=False)
         descricao = form.get('descricao')
         query = get_queryset_filter(self,form,descricao)
         return query

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['select'] = self.select
        context['form'] = self.form_class

        return context