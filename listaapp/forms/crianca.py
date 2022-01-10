# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.forms import *

from listaapp.models.crianca import Crianca
from listaapp.models.cei import Cei
from listaapp.models.tipo_chamado import TipoChamado


class CriancaForm(ModelForm):
    responsavel = ModelChoiceField(queryset=User.objects.filter(groups=1),required=False)
    cei = ModelChoiceField(queryset=Cei.objects.filter(desativado=False,excluido=False).order_by('nome'),
                             )
    colaborador = ModelMultipleChoiceField(queryset=User.objects.filter(is_superuser=True),required=False)
    solicitante = ModelChoiceField(queryset=User.objects.filter().order_by('username'))

    class Meta:
        model = Crianca
        exclude = ('usuario', 'excluido','cod','imagem','data_inicio','data_fim','status', 'desativado')

    def __init__(self, *args, **kwargs):
        super(CriancaForm,self).__init__(*args, **kwargs)
        # self.fields['propriedade'].widget = Select(
        #     choices=self.fields['propriedade'].choices,
        #     attrs={'class': 'form-control',
        #            })
        # self.fields['produto_utilizado'].widget = CheckboxSelectMultiple(
        #                     choices=self.fields['produto_utilizado'].choices,
        #                      attrs={'class': 'multiselect dropdown-toggle btn btn-default',
        #                             })
        # self.fields['equipamento_utilizado'].widget = SelectMultiple(
        #     choices=self.fields['equipamento_utilizado'].choices,
        #     attrs={'class': 'ui fluid  multiple search normal selection dropdown',
        #            })
        self.fields['cei'].widget = Select(
            choices=self.fields['cei'].choices,
            attrs={'class': 'form-control  small',
                   })
        # self.fields['tipo_crianca'].widget = Select(
        #     choices=self.fields['tipo_crianca'].choices,
        #
        #     attrs={'class': 'ui fluid   search normal selection dropdown',
        #            })
        self.fields['responsavel'].widget = Select(
            choices=self.fields['responsavel'].choices,

            attrs={'class': 'form-control',
                   })
        self.fields['solicitante'].widget = Select(
            choices=self.fields['solicitante'].choices,

            attrs={'class': 'form-control  small',
                   })
        self.fields['situacao'].widget = Select(
            choices=self.fields['situacao'].choices,

            attrs={'class': 'ui fluid   search normal selection dropdown',
                   })
        self.fields['colaborador'].widget = SelectMultiple(
            choices=self.fields['colaborador'].choices,
            # choices=User.objects.filter(is_superuser=True).values_list('id', 'username'),
            attrs={'class': 'ui fluid  multiple search normal selection dropdown',
                   })


class CriancaUsuarioForm(ModelForm):
    #cei = ModelMultipleChoiceField(queryset=Cei.objects.filter(desativado=False, excluido=False).order_by('nome'))
    cei = ModelMultipleChoiceField(
        queryset=Cei.objects.all(),
        widget=CheckboxSelectMultiple,
        required=True)

    class Meta:
        model = Crianca
        exclude = ('usuario','responsavel','excluido','cod','imagem','data_inicio','data_fim','status','produto_utilizado','produto_utilizado','servidor', 'desativado','data_inicio_atendimento')
       # fields = ( 'nome', 'cei','codigo' )





class CriancaUpdateForm(ModelForm):
    cei = ModelChoiceField(queryset=Cei.objects.filter(desativado=False, excluido=False).order_by('nome'))

    solicitante = ModelChoiceField(queryset=User.objects.filter().order_by('username'))

    class Meta:
        model = Crianca
        exclude = ('usuario', 'excluido','cod', 'imagem','data_inico','data_fim','desativado')

class CriancaAdminUpdateForm(ModelForm):
    cei = ModelChoiceField(queryset=Cei.objects.filter(desativado=False, excluido=False).order_by('nome'))
    solicitante = ModelChoiceField(queryset=User.objects.filter().order_by('username'))

    responsavel = ModelChoiceField(queryset=User.objects.filter(groups=1))
    colaborador = ModelMultipleChoiceField(queryset=User.objects.filter(is_superuser=True),required=False)

    class Meta:
            model = Crianca
            exclude = ('usuario', 'colaborador','excluido','cod', 'imagem','data_inico','data_fim','desativado','mensagem','data_inicio_atendimento')

    def __init__(self, *args, **kwargs):
        super(CriancaAdminUpdateForm,self).__init__(*args, **kwargs)
        self.fields['propriedade'].widget = Select(
            choices=self.fields['propriedade'].choices,
            attrs={'class': 'form-control ',
                   })
        self.fields['produto_utilizado'].widget = CheckboxSelectMultiple(
                            # choices=self.fields['produto_utilizado'].choices,
                            choices={},
                             attrs={'class': ' hidden',
                                    })
        self.fields['equipamento_utilizado'].widget = CheckboxSelectMultiple(
            # choices=self.fields['equipamento_utilizado'].choices,
            choices={},
            attrs={'class': ' hidden',
                   })
        self.fields['cei'].widget = Select(
            choices=self.fields['cei'].choices,
            attrs={'class': 'form-control  small',
                   })
        self.fields['tipo_crianca'].widget = Select(
            choices=self.fields['tipo_crianca'].choices,

            attrs={'class': 'ui fluid   search normal selection dropdown',
                   })
        self.fields['responsavel'].widget = Select(
            choices=self.fields['responsavel'].choices,

            attrs={'class': 'ui fluid   search normal selection dropdown',
                   })
        self.fields['solicitante'].widget = Select(
            choices=self.fields['solicitante'].choices,

            attrs={'class': 'form-control  small',
                   })
        self.fields['situacao'].widget = Select(
            choices=self.fields['situacao'].choices,

            attrs={'class': 'ui fluid   search normal selection dropdown',
                   })
        self.fields['colaborador'].widget = SelectMultiple(
                choices=self.fields['colaborador'].choices,
                attrs={'class': 'ui fluid  multiple search normal selection dropdown',
                       })
