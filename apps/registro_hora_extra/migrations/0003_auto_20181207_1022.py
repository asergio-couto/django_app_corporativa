# Generated by Django 2.1.4 on 2018-12-07 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro_hora_extra', '0002_registrohoraextra_funcionario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrohoraextra',
            name='funcionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='funcionarios.Funcionario'),
        ),
    ]
