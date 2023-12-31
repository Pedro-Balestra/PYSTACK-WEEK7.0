# Generated by Django 4.2.3 on 2023-07-03 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_conta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conta',
            name='banco',
            field=models.CharField(choices=[('NU', 'Nubank'), ('CE', 'Caixa economica'), ('BB', 'Banco Brasil')], max_length=2),
        ),
        migrations.AlterField(
            model_name='conta',
            name='tipo',
            field=models.CharField(choices=[('pf', 'Pessoa fisica'), ('pj', 'Pessoa juridica')], max_length=2),
        ),
    ]
