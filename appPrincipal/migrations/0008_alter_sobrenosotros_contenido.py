# Generated by Django 3.2.5 on 2021-09-01 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPrincipal', '0007_auto_20210901_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sobrenosotros',
            name='contenido',
            field=models.TextField(max_length=1000),
        ),
    ]
