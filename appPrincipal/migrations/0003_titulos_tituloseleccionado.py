# Generated by Django 3.2.5 on 2021-09-01 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPrincipal', '0002_auto_20210901_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='titulos',
            name='tituloSeleccionado',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]