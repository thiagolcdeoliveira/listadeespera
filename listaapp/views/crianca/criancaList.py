# coding=utf-8
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from django.views.generic import *

from listaapp.forms.crianca import CriancaForm
from listaapp.models.cei import Cei
from listaapp.models.crianca import Crianca
from listaapp.models.turma import Turma
from listaapp.views.crianca.caclulo import calculoTurma


class CriancaListView(PermissionRequiredMixin, ListView):
    permission_required = 'listaapp.view_crianca'
    template_name = 'crianca/crianca_list.html'
    model = Crianca
    queryset = Crianca
    paginate_by = 20
    form_class = CriancaForm
    select = {'todos': '0', 'codigo': '1', 'nome': '2', 'solicitante': '3', 'responsavel': '4',
              'descricao': '5'
              }
    ceis = Cei

    def get_queryset(self):

         form = self.request.GET
         if self.kwargs.get("pk"):
             self.queryset = Crianca.objects.filter(codigo=self.kwargs.get("pk"))
         else:
             self.queryset = Crianca.objects.all()
         self.ceis = self.ceis.objects.filter(desativado=False)
         descricao = form.get('descricao')
         query = get_queryset_filter(self,form,descricao)
         return query.order_by('status','-id').reverse()




    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['select'] = self.select
        context['ceis'] = self.ceis
        context['form'] = self.form_class
        return context


class CriancaPublicaListView(ListView):
    template_name = 'crianca/crianca_list.html'
    model = Crianca
    queryset = Crianca
    paginate_by = 20
    form_class = CriancaForm
    select = {'todos': '0', 'codigo': '1', 'nome_crianca': '2', 'solicitante': '3', 'responsavel': '4',
              'descricao': '5'
              }
    ceis = Cei
    turmas = Turma

    def get_queryset(self):

         form = self.request.GET
         if self.kwargs.get("pk"):
             self.queryset = Crianca.objects.filter(codigo=self.kwargs.get("pk"))
         else:
             self.queryset = Crianca.objects.all()
         self.ceis = self.ceis.objects.filter(desativado=False)
         self.turmas = self.turmas.objects.filter(desativado=False)

         descricao = form.get('descricao')
         # if descricao:
         query = get_queryset_filter(self,form,descricao)
         return query.order_by('desativado','-id').reverse()
         # return self.queryset.order_by('desativado','-id').reverse()




    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['select'] = self.select
        context['ceis'] = self.ceis
        context['turmas'] = self.turmas
        # context['turmas'] = calculoTurma(self.queryset[0].data_nasc)
        context['form'] = self.form_class
        return context




def get_queryset_filter(self,form,descricao):
    tipo = form.get('tipo')
    status = form.get('status')
    cei = form.get('cei')
    turma = form.get('turma')

    if tipo and descricao:
         if tipo == self.select.get("codigo"):
             # if descricao.isdigit():
             self.queryset = self.queryset.filter(codigo__icontains=form.get('descricao'))
         elif tipo == self.select.get("nome_crianca"):
             self.queryset = self.queryset.filter(Q(nome__icontains=descricao) |
             Q(sobrenome__icontains=descricao) )
         elif tipo == self.select.get("responsavel"):
             self.queryset = self.queryset.filter(Q(responsavel__username__icontains=descricao)|
                                                  Q(responsavel__first_name__icontains=descricao)|
                                                  Q(responsavel__last_name__icontains=descricao))
         elif form.get('tipo') == '0':
             if descricao.isdigit():
                 self.queryset = self.queryset.filter(
                      Q(pk=descricao) | Q(codigo__icontains=descricao)
                      | Q(nome__icontains=descricao) | Q( sobrenome__icontains=descricao)
                      | Q(responsavel__username__icontains=descricao)| Q(responsavel__last_name__icontains=descricao)
                      | Q(responsavel__first_name__icontains=descricao)
                      # | Q(cei__nome__icontains=descricao) | Q(turma__nome__icontains=descricao)

                 )
             else:
                 self.queryset = self.queryset.filter(
                     Q(codigo__icontains=descricao)
                     | Q(nome__icontains=descricao) | Q(sobrenome__icontains=descricao)
                     | Q(responsavel__username__icontains=descricao) | Q(responsavel__last_name__icontains=descricao)
                     | Q(responsavel__first_name__icontains=descricao)
                 )
    if form.get('status')=='1':
     self.queryset = self.queryset.filter(desativado=True)
    elif form.get('status')=='2':
     self.queryset = self.queryset.filter(desativado=False)
    # if form.get('data_incio'):
    #  self.queryset = self.queryset.filter(data_inicio__gte=form.get('data_incio'))
    # if form.get('data_fim'):
    #  self.queryset = self.queryset.filter(data_inicio__lte=form.get('data_fim'))
    # if form.get('data_incio_encerramento'):
    #  self.queryset = self.queryset.filter(data_fim__gte=form.get('data_incio_encerramento'))
    # if form.get('data_fim_encerramento'):
    #  self.queryset = self.queryset.filter(data_fim__lte=form.get('data_fim_encerramento'))
    if form.get('cei'):
        self.queryset = self.queryset.filter(cei__pk=form.get('cei'))
    if form.get('turma'):
        self.queryset = self.queryset.filter(turma__pk=form.get('turma'))

    return self.queryset.filter(excluido=False).order_by('id').reverse()


class CriancaPorResposavelListView(PermissionRequiredMixin, ListView):
    permission_required = 'listaapp.view_crianca'
    template_name = 'crianca/crianca_list.html'
    model = Crianca
    queryset = Crianca
    paginate_by = 20
    form_class = CriancaForm
    select = {'todos': '0', 'codigo': '1', 'nome': '2', 'solicitante': '3', 'responsavel': '4',
              'descricao': '5'
              }

    def get_queryset(self):

         form = self.request.GET
         # self.queryset = Crianca.objects.all()

         self.queryset = Crianca.objects.filter(responsavel=self.request.user)
         descricao = form.get('descricao')
         query = get_queryset_filter(self, form, descricao)
         return query


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['select'] = self.select
        context['form'] = self.form_class

        return context

# class TipoArquivoCreateView(PermissionRequiredMixin, CreateView):
class CriancaMeuListView(ListView):
    # permission_required = ADD_CHAMADO
    template_name = 'crianca/crianca_list.html'
    model = Crianca
    queryset = Crianca
    paginate_by = 20
    form_class = CriancaForm
    select = {'todos': '0', 'codigo': '1', 'nome': '2',  'responsavel': '4',
              'descricao': '5'
              }

    def get_queryset(self):

         form = self.request.GET
         self.queryset = Crianca.objects.filter((Q(solicitante=self.request.user)| Q(responsavel=self.request.user)), excluido=False)
         descricao = form.get('descricao')
         query = get_queryset_filter(self,form,descricao)
         return query

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['select'] = self.select
        context['form'] = self.form_class

        return context