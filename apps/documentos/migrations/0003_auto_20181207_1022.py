# Generated by Django 2.1.4 on 2018-12-07 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0002_documento_pertence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='pertence',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='funcionarios.Funcionario'),
        ),
    ]
