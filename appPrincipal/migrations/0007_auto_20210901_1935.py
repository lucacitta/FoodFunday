# Generated by Django 3.2.5 on 2021-09-01 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPrincipal', '0006_auto_20210901_1934'),
    ]

    operations = [
        migrations.RenameField(
            model_name='titulos',
            old_name='tituloSeleccionado',
            new_name='seleccionado',
        ),
        migrations.AddField(
            model_name='sobrenosotros',
            name='seleccionado',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]