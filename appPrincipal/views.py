from appPrincipal.models import Contacto, Especiales, Galeria, Horarios, Menu, Novedades, Redes, SobreNosotros, Titulos
from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
    titulo=Titulos.objects.all()
    sobreNosotros = SobreNosotros.objects.all()
    especiales = Especiales.objects.all()
    menu=Menu.objects.all()
    galeria=Galeria.objects.all()
    novedades=Novedades.objects.all()
    redes=Redes.objects.all()
    contacto=Contacto.objects.all()
    horarios=Horarios.objects.all
    if request.method=='POST':
        data=request.POST
        nombre=data.get('nombre')
        email=data.get('email')
        mensaje=data.get('mensaje')





    return render(
        request,
        'index.html',
        {'titulo':titulo,
        'sobreNosotros':sobreNosotros,
        'especiales':especiales,
        'menu':menu,
        'galeria':galeria,
        'novedades':novedades,
        'redesSociales':redes,
        'contactos':contacto,
        'horarios':horarios,
        })