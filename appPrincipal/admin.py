from django.contrib import admin
from . import models
from django.contrib.auth.models import Group

# Register your models here.
class TitulosAdmin(admin.ModelAdmin):
    list_display = ('tituloPrincipal','palabrasCambiantes','subtitulo','subtituloTexto')
admin.site.register(models.Titulos, TitulosAdmin)


class SobreNosotrosAdmin(admin.ModelAdmin):
    list_display = ('titulo','subtitulo','contenido','imagenPrincipal','imagenSecundaria')
admin.site.register(models.SobreNosotros, SobreNosotrosAdmin)


class EspecialesAdmin(admin.ModelAdmin):
    list_display = ('titulo','contenido','imagen')
    list_filter = ('titulo', )
admin.site.register(models.Especiales, EspecialesAdmin)


class MenuAdmin(admin.ModelAdmin):
    fields = ('titulo','descripcion','precio','tipo','admin_photo')
    list_display = ('titulo','descripcion','precio','tipo','admin_photo')
    list_filter = ('titulo','tipo')
    readonly_fields = ('admin_photo',)
admin.site.register(models.Menu, MenuAdmin)


class GaleriaAdmin(admin.ModelAdmin):
    list_display = ('imagen_1','imagen_2','imagen_3','imagen_4','imagen_5','imagen_6','imagen_7','imagen_8','imagen_9','imagen_10')
admin.site.register(models.Galeria, GaleriaAdmin)


class NovedadesAdmin(admin.ModelAdmin):
    list_display = ('titulo','contenido','imagen','activado')
    list_filter = ('titulo','activado')
    list_editable = ('activado',)
admin.site.register(models.Novedades, NovedadesAdmin)


class RedesAdmin(admin.ModelAdmin):
    list_display = ('contenido','facebook','twitter','instagram')
admin.site.register(models.Redes, RedesAdmin)


class ContactoAdmin(admin.ModelAdmin):
    list_display = ('direccion','telefono','email')
admin.site.register(models.Contacto, ContactoAdmin)


class HorariosAdmin(admin.ModelAdmin):
    list_display = ('lunes','martes','miercoles','jueves','viernes','sabado','domingo')
admin.site.register(models.Horarios, HorariosAdmin)


admin.site.unregister(Group)
admin.site.site_header='Administrador'