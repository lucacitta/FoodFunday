# Generated by Django 3.2.5 on 2021-09-04 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPrincipal', '0022_auto_20210903_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=2),
        ),
    ]
