# Generated by Django 3.2.9 on 2021-12-15 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do Bairro', max_length=200, verbose_name='Nome do Bairro')),
                ('excluido', models.BooleanField(default=False, verbose_name='Excluído')),
                ('desativado', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Bairro',
                'verbose_name_plural': 'Bairros',
                'permissions': (('baseapp_add_bairro', 'Adicionar Bairro'), ('baseapp_detail_bairro', 'Visualizar Bairro'), ('baseapp_delete_bairro', 'Excluir Bairro')),
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do endereço ', max_length=200, verbose_name='Nome do Endereço')),
                ('rua', models.CharField(help_text='Nome da Rua ', max_length=200, verbose_name='Nome da Rua')),
                ('coordenadas', models.CharField(blank=True, help_text='Nome do Coordenadas ', max_length=200, verbose_name='Coordenadas')),
                ('excluido', models.BooleanField(default=False, verbose_name='Excluído')),
                ('desativado', models.BooleanField(default=False)),
                ('bairro', models.ForeignKey(blank=True, help_text='Bairro', null=True, on_delete=django.db.models.deletion.SET_NULL, to='baseapp.bairro', verbose_name='Bairro')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Endereco',
                'verbose_name_plural': 'Enderecos',
                'permissions': (('baseapp_add_endereco', 'Adicionar Endereço'), ('baseapp_detail_endereco', 'Visualizar Endereço'), ('baseapp_delete_endereco', 'Excluir Endereço')),
            },
        ),
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='imagem/mensagem')),
                ('excluido', models.BooleanField(default=False, verbose_name='Excluído')),
                ('desativado', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Imagem',
                'verbose_name_plural': 'Imagens',
                'permissions': (('baseapp_add_imagem', 'Adicionar imagem'), ('baseapp_detail_imagens', 'Visualizar imagem'), ('baseapp_delete_imagem', 'Excluir imagem')),
            },
        ),
        migrations.CreateModel(
            name='TipoPropriedade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do Tipo de Propriedade ', max_length=200, verbose_name='Nome do Tipo de propriedade')),
                ('descricao', models.CharField(help_text='Descrição do Tipo de Propriedade', max_length=200, verbose_name='descricção do tipo de propriedade')),
                ('excluido', models.BooleanField(default=False, verbose_name='Excluído')),
                ('desativado', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Tipo de Propriedade',
                'verbose_name_plural': 'Tipos de Propriedades',
                'permissions': (('baseapp_add_tipo_propriedade', 'Adicionar Tipo de propriedade'), ('baseapp_detail_tipo_propriedade', 'Visualizar Tipo de propriedade'), ('baseapp_delete_tipo_propriedade', 'Excluir tipo de propriedade')),
            },
        ),
        migrations.CreateModel(
            name='TipoNotificacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do Tipo de Notificação', max_length=200, verbose_name='Nome do Tipo de Notificação')),
                ('descricao', models.CharField(help_text='Descrição do Conteudo da Notificação', max_length=200, verbose_name='Descrição do Conteudo da Notificação')),
                ('link', models.CharField(blank=True, help_text='Link da Notificação', max_length=200, verbose_name='Link')),
                ('icon', models.CharField(help_text='Icone da Notificação', max_length=200, verbose_name='icon')),
                ('excluido', models.BooleanField(default=False, verbose_name='Excluído')),
                ('desativado', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Tipo Notificacao',
                'verbose_name_plural': 'Tipos de notificacao',
                'permissions': (('baseapp_add_tipo_notificacao', 'Adicionar tipo notificacao'), ('baseapp_detail_tipo_notificacao', 'Visualizar tipo notificacao'), ('baseapp_delete_tipo_notificacao', 'Excluir tipo notificacao')),
            },
        ),
        migrations.CreateModel(
            name='TipoGrafico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do Tipo de Grafico.', max_length=200, verbose_name='Nome do Tipo do grafico')),
                ('descricao', models.CharField(help_text='Nome do Tipo de Grafico.', max_length=200, verbose_name='Descricao/codigo grafico')),
                ('excluido', models.BooleanField(default=False, verbose_name='Excluído')),
                ('desativado', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Tipo de grafico',
                'verbose_name_plural': 'Tipos de Graficos',
                'permissions': (('baseapp_add_tipo_de_grafico', 'Adicionar tipo de grafico'), ('baseapp_detail_tipo_de_grafico', 'Visualizar tipo  de grafico'), ('baseapp_delete_tipo_De_grafico', 'Excluir tipo de grafico')),
            },
        ),
        migrations.CreateModel(
            name='TipoChamado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do Produto (Exemplo: Leite, Ovo , etc .).', max_length=200, verbose_name='Nome do Produto')),
                ('imagem', models.ImageField(blank=True, upload_to='chamado/imagem')),
                ('excluido', models.BooleanField(default=False, verbose_name='Excluído')),
                ('desativado', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Tipo de Chamado',
                'verbose_name_plural': 'Tipo de Chamados',
                'permissions': (('baseapp_add_tipo_chamado', 'Adicionar Chamado'), ('baseapp_detail_tipo_chamado', 'Visualizar Chamado'), ('baseapp_delete_tipo_chamado', 'Excluir Chamado')),
            },
        ),
        migrations.CreateModel(
            name='Tamanho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do tamanaho.', max_length=200, verbose_name='Nome Tamanho')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição do Tamanho')),
                ('excluido', models.BooleanField(default=False, verbose_name='Excluído')),
                ('desativado', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Tamanho',
                'verbose_name_plural': 'Tamanho',
                'permissions': (('baseapp_add_tamanho', 'Adicionar Tamanho'), ('baseapp_detail_tamanho', 'Visualizar Tamanho'), ('baseapp_delete_tamanho', 'Excluir tamanho')),
            },
        ),
        migrations.CreateModel(
            name='Situacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome da Situacao.', max_length=200, verbose_name='Situaçao')),
                ('excluido', models.BooleanField(default=False, verbose_name='Excluído')),
                ('desativado', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Situaçao',
                'verbose_name_plural': 'Situaçao',
                'permissions': (('baseapp_add_situacao', 'Adicionar Situação'), ('baseapp_detail_situacao', 'Visualizar Situação'), ('baseapp_delete_situacao', 'Excluir Situação')),
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome da Configuração', max_length=200, verbose_name='Nome da Configuração')),
                ('logo', models.ImageField(blank=True, help_text='Logo Principal', null=True, upload_to='imagem/settings', verbose_name='Logo')),
                ('logo_baixa', models.ImageField(blank=True, help_text='Logo Baixa Resolução', null=True, upload_to='imagem/settings', verbose_name='Logo Baixa Resolução')),
                ('imagem_login', models.ImageField(blank=True, help_text='Imagem Login', null=True, upload_to='imagem/settings', verbose_name='Imagem Login')),
                ('imagem_cadastro', models.ImageField(blank=True, help_text='Imagem Cadastro', null=True, upload_to='imagem/settings', verbose_name='Imagem Cadastro')),
                ('cor', models.CharField(blank=True, help_text='Cor do Menu', max_length=200, verbose_name='Cor de Menu')),
                ('numero', models.BooleanField(help_text='Numero para Virada', verbose_name='Numero para Virada')),
                ('excluido', models.BooleanField(default=False, verbose_name='Excluído')),
                ('desativado', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
                ('usuario_recebe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usuario_recebe_settings', to=settings.AUTH_USER_MODEL, verbose_name='Usuário Recebe')),
            ],
            options={
                'verbose_name': 'Settings',
                'verbose_name_plural': 'Settings',
                'permissions': (('baseapp_add_settings', 'Adicionar settings'), ('baseapp_detail_settings', 'Visualizar settings'), ('baseapp_delete_settings', 'Excluir settings')),
            },
        ),
        migrations.CreateModel(
            name='Secretaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome da Secretaria (Exemplo: Administraçao, Governo, etc .).', max_length=200, verbose_name='Nome da Secretaria')),
                ('excluido', models.BooleanField(default=False, verbose_name='Excluído')),
                ('desativado', models.BooleanField(default=False)),
                ('responsavel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='responsavel_usuario_secretaria', to=settings.AUTH_USER_MODEL, verbose_name='Servidor Responsavel')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Secretaria',
                'verbose_name_plural': 'Secretarias',
                'permissions': (('baseapp_add_secretaria', 'Adicionar Secretaria'), ('baseapp_detail_secretaria', 'Visualizar Secretaria'), ('baseapp_delete_secretaria', 'Excluir Secretaria')),
            },
        ),
        migrations.CreateModel(
            name='Propriedade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, help_text='Nome da Propriedade', max_length=200, verbose_name='Nome da Propriedade')),
                ('numero_patrimonio', models.CharField(blank=True, help_text='Cód da Propriedade', max_length=200, verbose_name='Cód da Propriedade')),
                ('descricao', models.TextField(blank=True, max_length=200, verbose_name='Descrição')),
                ('excluido', models.BooleanField(default=False, verbose_name='Excluído')),
                ('desativado', models.BooleanField(default=False)),
                ('endereco', models.ForeignKey(blank=True, help_text='Endereço da Propriedade', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='endereco_propriedade', to='baseapp.endereco', verbose_name='Endereço da Propriedade')),
                ('tipo_propriedade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='baseapp.tipopropriedade', verbose_name='Tipo de Propriedade')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'propriedade',
                'verbose_name_plural': 'propriedades',
                'permissions': (('baseaap_add_propriedade', 'Adicionar Propriedade'), ('baseaap_detail_propriedade', 'Visualizar Propriedade'), ('baseapp_delete_propriedade', 'Excluir Propriedade')),
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do Produto (Exemplo: Leite, Ovo , etc .).', max_length=200, verbose_name='Nome do Produto')),
                ('descricao', models.CharField(help_text='Descricao do Produto (Exemplo: Leite, Ovo , etc .).', max_length=200, verbose_name='Descricao do Produto')),
                ('excluido', models.BooleanField(default=False, verbose_name='Excluído')),
                ('desativado', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'permissions': (('baseapp_add_produto', 'Adicionar Produto'), ('baseapp_detail_produto', 'Visualizar Produto'), ('baseapp_delete_produto', 'Excluir Produto')),
            },
        ),
        migrations.CreateModel(
            name='Prioridade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome da Prioridade.', max_length=200, verbose_name='Nome')),
                ('sla', models.CharField(help_text='Sla de atendimento.', max_length=200, verbose_name='SLA')),
                ('excluido', models.BooleanField(default=False, verbose_name='Excluído')),
                ('desativado', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Prioridade',
                'verbose_name_plural': 'Prioridades',
                'permissions': (('baseapp_add_prioridade', 'Adicionar Prioridade'), ('baseapp_detail_prioridade', 'Visualizar prioridade'), ('baseapp_delete_prioridade', 'Excluir prioridade')),
            },
        ),
        migrations.CreateModel(
            name='Notificacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, help_text='Nome da Notificação', max_length=200, verbose_name='Nome da Notificação')),
                ('link', models.CharField(blank=True, help_text='Link da Notificação', max_length=200, verbose_name='Link')),
                ('destino', models.CharField(blank=True, help_text='Destino da Notificação', max_length=200, verbose_name='Destino')),
                ('prioridade', models.CharField(blank=True, help_text='prioridade da Notificação', max_length=200, verbose_name='Prioridade')),
                ('data', models.DateField(auto_now=True, help_text='Data da Notificação', verbose_name='Data')),
                ('excluido', models.BooleanField(default=False, verbose_name='Excluído')),
                ('desativado', models.BooleanField(default=False)),
                ('tipo_notificacao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='baseapp.tiponotificacao', verbose_name='Tipo a Notificar')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
                ('usuario_recebe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usuario_recebe', to=settings.AUTH_USER_MODEL, verbose_name='Usuário a Notificar')),
            ],
            options={
                'verbose_name': 'Notificação',
                'verbose_name_plural': 'Notificações',
                'permissions': (('baseapp_add_notificacao', 'Adicionar Notificação'), ('baseapp_detail_notificacao', 'Visualizar Notificação'), ('baseapp_delete_notificaao', 'Excluir Notificação')),
            },
        ),
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(blank=True, help_text='Adicione um imagem', max_length=200, null=True, verbose_name='Descricao')),
                ('data', models.DateTimeField(auto_now=True, null=True)),
                ('excluido', models.BooleanField(default=False, verbose_name='Excluído')),
                ('desativado', models.BooleanField(default=False)),
                ('imagem', models.ManyToManyField(blank=True, to='baseapp.Imagem')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Mensagem',
                'verbose_name_plural': 'Mensagens',
                'permissions': (('baseapp_add_mensagem', 'Adicionar mensagem'), ('baseapp_detail_mensagem', 'Visualizar mensagem'), ('baseapp_delete_mensagem', 'Excluir mensagem')),
            },
        ),
        migrations.CreateModel(
            name='Grafico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do Grafico.', max_length=200, verbose_name='Nome do Grafico')),
                ('consulta', models.TextField(help_text='Consulta do Grafico.', max_length=2000, verbose_name='Consulta do Grafico')),
                ('excluido', models.BooleanField(default=False, verbose_name='Excluído')),
                ('desativado', models.BooleanField(default=False)),
                ('tipo_grafico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='baseapp.tipografico', verbose_name='TipoDoGrafico')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'grafico',
                'verbose_name_plural': 'graficos',
                'permissions': (('baseapp_add_grafico', 'Adicionar Grafico'), ('baseapp_detail_grafico', 'Visualizar Grafico'), ('baseapp_delete_grafico', 'Excluir Grafico')),
            },
        ),
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do Produto (Exemplo: Leite, Ovo , etc .).', max_length=200, verbose_name='Nome do Equipamento')),
                ('excluido', models.BooleanField(default=False, verbose_name='Excluído')),
                ('desativado', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Equipamento',
                'verbose_name_plural': 'Equipamentos',
                'permissions': (('baseapp_add_equipamento', 'Adicionar Equipamento'), ('baseapp_detail_equipamento', 'Visualizar Equipamento'), ('baseapp_delete_equipamento', 'Excluir Equipamento')),
            },
        ),
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, help_text='Nome do Dashboard', max_length=200, verbose_name='Nome do Dashboard')),
                ('ordem', models.PositiveIntegerField(null=True)),
                ('excluido', models.BooleanField(default=False, verbose_name='Excluído')),
                ('desativado', models.BooleanField(default=False)),
                ('grafico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='baseapp.grafico', verbose_name='Grafico')),
                ('tamanho', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='baseapp.tamanho', verbose_name='Tamanho')),
                ('tipo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='baseapp.tipografico', verbose_name='Tipo Grafico')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
                ('usuario_recebe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usuario_recebe_dashboard', to=settings.AUTH_USER_MODEL, verbose_name='Usuário Recebe')),
            ],
            options={
                'verbose_name': 'Dashboard',
                'verbose_name_plural': 'Dashboards',
                'permissions': (('sgapapp_add_dashaboard', 'Adicionar Dashboard'), ('sgapapp_detail_dashboard', 'Visualizar Dashboard'), ('baseapp_delete_dashboard', 'Excluir dashboard')),
            },
        ),
        migrations.CreateModel(
            name='ConfiguracaoEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Defina um nome para configuração', max_length=200, verbose_name='Nome da Configuração')),
                ('html', models.TextField(help_text='Defina o Html para corpo do email', max_length=4000, verbose_name='HTML')),
                ('excluido', models.BooleanField(default=False, verbose_name='Excluído')),
                ('desativado', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Configuracao de email',
                'verbose_name_plural': 'Configuracoes de emails',
                'permissions': (('baseapp_add_config_email', 'Adicionar Configuração de Email'), ('baseapp_detail_config_email', 'Visualizar Configuração de Email'), ('baseapp_delete_config_email', 'Excluir Configuração de Email')),
            },
        ),
    ]
