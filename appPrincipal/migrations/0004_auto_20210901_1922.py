# Generated by Django 3.2.5 on 2021-09-01 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPrincipal', '0003_titulos_tituloseleccionado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='titulos',
            name='subtituloTextp',
        ),
        migrations.AddField(
            model_name='titulos',
            name='subtituloTexto',
            field=models.CharField(default='pepe', max_length=200),
            preserve_default=False,
        ),
    ]