# Generated by Django 3.2.9 on 2021-12-15 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('baseapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cei',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do Setor (Exemplo: TI, Compras , etc .).', max_length=200, verbose_name='Nome do Setor')),
                ('excluido', models.BooleanField(default=False, verbose_name='Excluído')),
                ('desativado', models.BooleanField(default=False)),
                ('secretaria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='baseapp.secretaria', verbose_name='Setor Superior')),
                ('servidor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='servidor_usuario_setor', to=settings.AUTH_USER_MODEL, verbose_name='Servidor Responsavel')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Cei',
                'verbose_name_plural': 'Ceis',
                'permissions': (('lisapp_add_cei', 'Adicionar Cei'), ('listaapp_detail_cei', 'Visualizar Cei'), ('listaapp_delete_cei', 'Excluir Cei')),
            },
        ),
        migrations.CreateModel(
            name='Crianca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=200, verbose_name='Codigo da Criança')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=200, verbose_name='Sobrenomenome')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, null=True)),
                ('data_nasc', models.DateField(blank=True)),
                ('data_retirada_fila', models.DateTimeField(null=True)),
                ('autorizacao', models.BooleanField(default=False, verbose_name='Excluído')),
                ('excluido', models.BooleanField(default=False, verbose_name='Excluído')),
                ('desativado', models.BooleanField(default=False)),
                ('cei', models.ForeignKey(help_text='Cei desejado .', null=True, on_delete=django.db.models.deletion.SET_NULL, to='listaapp.cei', verbose_name='Cei')),
                ('responsavel', models.ForeignKey(help_text='Servidor responsavel data TI pelo chamado .', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='responsavel_usuario', to=settings.AUTH_USER_MODEL, verbose_name='Responsavel')),
                ('situacao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='baseapp.situacao')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Criança',
                'verbose_name_plural': 'Crianças',
                'permissions': (('listaapp_add_crianca', 'Adicionar Crianca'), ('listaapp_detail_crianca', 'Visualizar Crianca'), ('listaapp_delete_crianca', 'Excluir Crianca'), ('listaapp_list_crianca', 'Listar Crianca')),
            },
        ),
    ]
