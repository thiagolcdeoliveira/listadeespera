# Generated by Django 3.2.9 on 2021-12-22 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listaapp', '0004_auto_20211222_1043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crianca',
            name='turma',
        ),
    ]
