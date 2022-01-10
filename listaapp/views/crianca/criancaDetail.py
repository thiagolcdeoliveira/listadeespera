# coding=utf-8
from django.views.generic import *


from baseapp.forms.mensagem import MensagemForm
from listaapp.models.crianca import Crianca


# class TipoArquivoCreateView(PermissionRequiredMixin, CreateView):
class CriancaDetailView( DetailView):
    # permission_required = ADD_CHAMADO

    template_name = 'crianca/crianca_detail.html'
    model = Crianca

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MensagemForm()
        return context

class ChamadoUsuarioDetailView( DetailView):
    # permission_required = ADD_CHAMADO

    template_name = 'crianca/chamado_usuario_detail.html'
    model = Crianca

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MensagemForm()
        return context