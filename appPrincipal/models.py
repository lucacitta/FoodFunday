from django.db import models
from django.db.models.base import Model
from django.db.models.fields.files import ImageField
from django.utils.safestring import mark_safe

# Create your models here.
class Titulos (models.Model):
    tituloPrincipal= models.CharField(max_length=80)
    palabrasCambiantes=models.CharField(max_length=80)
    subtitulo=models.CharField(max_length=80)
    subtituloTexto=models.CharField(max_length=200)

    class Meta:
        verbose_name= 'titulo'
        verbose_name_plural= 'titulos'

    def __str__(self):
        return self.tituloPrincipal

class SobreNosotros(models.Model):
    titulo = models.CharField(max_length=80)
    subtitulo = models.CharField(max_length=100)
    contenido = models.TextField(max_length=1000)
    seleccionado = models.BooleanField()
    imagenPrincipal = models.ImageField()
    imagenSecundaria = models.ImageField()

    class Meta:
        verbose_name= 'Sobre Nosotro'

    def __str__(self):
        return self.titulo

class Especiales(models.Model):
    titulo = models.CharField(max_length=80)
    contenido = models.CharField(max_length=300)
    imagen = models.ImageField()

    class Meta:
        verbose_name= 'Especiale'

    def __str__(self):
        return self.titulo




entradas = 'Entradas'
principal = 'Plato Principal'
postres = 'Postres'
bebidas = 'Bebidas'

elecciones = [
    (entradas, ('Entradas')),
    (principal, ('Principal')),
    (postres, ('Postres')),
    (bebidas, ('Bebidas')),
    ]

class Menu(models.Model):
    titulo=models.CharField(max_length=80)
    descripcion=models.CharField(max_length=45)
    descripcion2=models.CharField(max_length=45)
    precio=models.IntegerField()
    imagen=models.ImageField()
    tipo=models.CharField(max_length=40, choices=elecciones)

    def admin_photo(self):
        return mark_safe('<img src"{}" width="100"/>'.format(self.imagen.url))
    admin_photo.short_description = 'imagen'
    admin_photo.allow_tags = True

    class Meta:
        verbose_name_plural='Menu'

    def __str__(self):
        return self.titulo

class Galeria(models.Model):
    titulo=models.CharField(max_length=20)
    descripcion=models.CharField(max_length=200)
    imagen_1=models.ImageField()
    imagen_1_Descripcion=models.CharField(max_length=40)

    imagen_2=models.ImageField()
    imagen_2_Descripcion=models.CharField(max_length=40)

    imagen_3=models.ImageField()
    imagen_3_Descripcion=models.CharField(max_length=40)

    imagen_4=models.ImageField()
    imagen_4_Descripcion=models.CharField(max_length=40)

    imagen_5=models.ImageField()
    imagen_5_Descripcion=models.CharField(max_length=40)

    imagen_6=models.ImageField()
    imagen_6_Descripcion=models.CharField(max_length=40)

    imagen_7=models.ImageField()
    imagen_7_Descripcion=models.CharField(max_length=40)

    imagen_8=models.ImageField()
    imagen_8_Descripcion=models.CharField(max_length=40)

    imagen_9=models.ImageField()
    imagen_9_Descripcion=models.CharField(max_length=40)

    imagen_10=models.ImageField()
    imagen_10_Descripcion=models.CharField(max_length=40)

    class Meta:
        verbose_name_plural='Galeria'

    def __str__(self):
        return self.titulo

class Novedades(models.Model):
    titulo= models.CharField(max_length=25)
    contenido= models.CharField(max_length=200)
    creado= models.DateTimeField(auto_now_add=True)
    imagen= models.ImageField()
    activado= models.BooleanField()

    class Meta:
        verbose_name_plural='Novedades'

    def __str__(self):
        return self.titulo

class Redes(models.Model):
    contenido= models.CharField(max_length=300)
    facebook= models.CharField(max_length=100)
    twitter= models.CharField(max_length=100)
    instagram= models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='Redes'

    def __str__(self):
        return self.facebook

class Contacto(models.Model):
    direccion= models.CharField(max_length=200)
    telefono= models.IntegerField()
    email= models.EmailField(max_length=100)

    class Meta:
        verbose_name_plural='Contacto'

    def __str__(self):
        return self.email

class Horarios(models.Model):
    lunes=models.CharField(max_length=100)
    martes=models.CharField(max_length=100)
    miercoles=models.CharField(max_length=100)
    jueves=models.CharField(max_length=100)
    viernes=models.CharField(max_length=100)
    sabado=models.CharField(max_length=100)
    domingo=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='Horarios'

    def __str__(self):
        return self.lunes