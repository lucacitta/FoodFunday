# Generated by Django 3.2.5 on 2021-09-02 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPrincipal', '0014_galeria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='galeria',
            old_name='imagen1',
            new_name='imagen_1',
        ),
        migrations.RenameField(
            model_name='galeria',
            old_name='imagen10',
            new_name='imagen_10',
        ),
        migrations.RenameField(
            model_name='galeria',
            old_name='imagen2',
            new_name='imagen_2',
        ),
        migrations.RenameField(
            model_name='galeria',
            old_name='imagen3',
            new_name='imagen_3',
        ),
        migrations.RenameField(
            model_name='galeria',
            old_name='imagen4',
            new_name='imagen_4',
        ),
        migrations.RenameField(
            model_name='galeria',
            old_name='imagen5',
            new_name='imagen_5',
        ),
        migrations.RenameField(
            model_name='galeria',
            old_name='imagen6',
            new_name='imagen_6',
        ),
        migrations.RenameField(
            model_name='galeria',
            old_name='imagen7',
            new_name='imagen_7',
        ),
        migrations.RenameField(
            model_name='galeria',
            old_name='imagen8',
            new_name='imagen_8',
        ),
        migrations.RenameField(
            model_name='galeria',
            old_name='imagen9',
            new_name='imagen_9',
        ),
        migrations.AddField(
            model_name='galeria',
            name='imagen_10_Descripcion',
            field=models.CharField(default='corta descripcion del producto', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='galeria',
            name='imagen_1_Descripcion',
            field=models.CharField(default='corta descripcion del producto', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='galeria',
            name='imagen_2_Descripcion',
            field=models.CharField(default='corta descripcion del producto', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='galeria',
            name='imagen_3_Descripcion',
            field=models.CharField(default='corta descripcion del producto', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='galeria',
            name='imagen_4_Descripcion',
            field=models.CharField(default='corta descripcion del producto', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='galeria',
            name='imagen_5_Descripcion',
            field=models.CharField(default='corta descripcion del producto', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='galeria',
            name='imagen_6_Descripcion',
            field=models.CharField(default='corta descripcion del producto', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='galeria',
            name='imagen_7_Descripcion',
            field=models.CharField(default='corta descripcion del producto', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='galeria',
            name='imagen_8_Descripcion',
            field=models.CharField(default='corta descripcion del producto', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='galeria',
            name='imagen_9_Descripcion',
            field=models.CharField(default='corta descripcion del producto', max_length=40),
            preserve_default=False,
        ),
    ]