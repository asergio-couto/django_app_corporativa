# Generated by Django 2.1.4 on 2018-12-06 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
        ('funcionarios', '0003_funcionario_departamentos'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='empresa',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='empresas.Empresa'),
        ),
    ]
