# coding=utf-8
from PIL import Image
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.urls import reverse
from base.settings import MEDIA_ROOT
from listaapp.forms.crianca import CriancaForm, CriancaUsuarioForm
from listaapp.models.cei import Cei
from listaapp.models.crianca import Crianca
from baseapp.models.email import ConfiguracaoEmail
from django.views.generic.edit import CreateView

from baseapp.models.notificacao import Notificacao
from baseapp.models.tipo_notificacao import TipoNotificacao
#from baseapp.views.chamado.chamadoQrcode import get_qrcode
from baseapp.views.email import  send_mail
from listaapp.forms.crianca import CriancaForm
from listaapp.models.crianca import Crianca


class CriancaCreateView(LoginRequiredMixin, CreateView):
    # permission_required = ADD_CHAMADO
    template_name = 'crianca/crianca_admin_form.html'
    template_name_email = 'includes/email.html'
    model = Crianca
    form_class = CriancaForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.usuario = self.request.user
        if not self.request.user.is_superuser:
            self.object.responsavel = self.request.user
        self.object.save()

        # if self.request.POST.get('notificar'):
        #     print("Notificar Solicitante")
        #     context = {}
        #     context['id'] =  self.object.id
        #     context['solicitante'] =  self.object.solicitante.username
        #     if  self.object.responsavel:
        #         context['responsavel'] =  self.object.responsavel.username
        #     else:
        #         context['responsavel'] =  'Não Definido'
        #     context['descricao'] =  self.object.descricao
        #     context['titulo'] =  'Cadastro de Chamado'
        #     chamado, created = ConfiguracaoEmail.objects.get_or_create(nome="cadastrar_admin_chamado")
        #     chamado = replece_html_convert(chamado.html,self.object,self.request)
        #     send_mail('Cadastro de Chamado #'+str(self.object.id),chamado,[self.object.solicitante.email,])

        # if self.object.tipo_chamado.imagem:
        #     logo = Image.open(MEDIA_ROOT + '/' + self.object.tipo_chamado.imagem.name)
        # else:
        #     logo = Image.open(MEDIA_ROOT + '/chamado/imagem/logoti.png')

        # get_qrcode(self.object.setor, self.object.id, logo,self.request)
        # get_qrcode(self.object.setor.nome,self.object.id,logo,self.request)
        # if self.object.responsavel:
        #     tipo_notificacao, created = TipoNotificacao.objects.get_or_create(nome="Chamado Atribuido")
        #     link = reverse("chamado-detail",kwargs={'pk': self.object.id})
        #     notificacao = Notificacao(tipo_notificacao=tipo_notificacao, nome="#%s - %s" %(self.object.id,self.object.nome),
        #                                        usuario_recebe=self.object.responsavel, usuario=self.request.user,
        #                                        prioridade=self.object.prioridade.nome,
        #                               link=link)
        #     notificacao.save()


        return super(CriancaCreateView, self).form_valid(form)


    def form_invalid(self, form):
        '''

        :param self:
        :param form: erro no form
        :return: retorna o erro no cadastro
        '''
        print(form.errors)

        return super(CriancaCreateView, self).form_invalid(form)
def replece_html_convert(chamado,object,request):

    chamado=chamado.replace("{{nome}}",object.nome)
    # chamado=chamado.replace("{{prioridade}}",object.prioridade.nome)
    chamado=chamado.replace("{{id}}",str(object.id))
    print(object.responsavel)
    if object.responsavel:
        chamado=chamado.replace("{{responsavel}}",object.responsavel.username)
    chamado=chamado.replace("{{usuario}}",object.usuario.username)
    # chamado=chamado.replace("{{solicitante}}",object.solicitante.username)
    # url = 'http://' + request.META.get('HTTP_HOST') + reverse('chamado-detail',kwargs={'pk':object.id})
    # chamado=chamado.replace("{{url}}",url)
    return chamado

class CriancaUsuarioCreateView(LoginRequiredMixin, CreateView):
    # permission_required = ADD_CHAMADO
    template_name = 'crianca/crianca_usuario_form.html'
    template_name_email = 'includes/email.html'
    model = Crianca
    form_class = CriancaUsuarioForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.usuario = self.request.user
        self.object.responsavel = self.request.user
        self.object.save()
        context = {}
        context['id'] =  self.object.id
        context['responsavel'] =  self.object.responsavel.username
        # context['responsavel'] =  self.object.responsavel.username
        # context['descricao'] =  self.object.descricao
        context['titulo'] =  'Criança de Cadastrada'
        chamado, created = ConfiguracaoEmail.objects.get_or_create(nome="cadastrar_crianca_fila")
        chamado = replece_html_convert(chamado.html,self.object,self.request)
        send_mail('Cadastro de Criança #'+str(self.object.id),chamado,[self.object.responsavel.email,])
        return super(CriancaUsuarioCreateView, self).form_valid(form)

    def form_invalid(self, form):
        '''

        :param self:
        :param form: erro no form
        :return: retorna o erro no cadastro
        '''

        print(form.errors)

        return super(CriancaUsuarioCreateView, self).form_invalid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ceis'] = Cei.objects.filter(desativado=False)
        context['form'] = self.form_class
        return context