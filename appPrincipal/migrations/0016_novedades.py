# Generated by Django 3.2.5 on 2021-09-02 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPrincipal', '0015_auto_20210902_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='novedades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=25)),
                ('contenido', models.CharField(max_length=200)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('imagen', models.ImageField(upload_to='')),
                ('activado', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Novedades',
            },
        ),
    ]
