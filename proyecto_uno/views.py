from django.http import HttpResponse
from django.template import Template, Context
import datetime

#views
#estas son vistas simples creadas como practica, para ver el funcionamiento de las vistas
"""
def index(httpRequest):
    return HttpResponse("Bienvenido al index de la aplicacion.")

def about(httpRequest):
    return HttpResponse("Esta es la pagina sobre nosotros")

def contacto(httpRequest):
    return HttpResponse("Esta es la pagina de contacto")

def usuario(httpRequest, nombre):

    fecha = datetime.datetime.now()

    return HttpResponse("Bienvenido %s de nuevo a su perfil. La fecha es: %s" %(nombre, fecha))

def edad(httpRequest, edad):
    return HttpResponse("Su edad es: %s años" %edad)

"""

#vistas creadas con templates
def index(httpRequest):
    #carga doc
    doc = open("C:/Users/Santiago/PycharmProjects/proyectos-django/proyecto_uno/proyecto_uno/templates/index.html")
    #crea el template
    template = Template(doc.read())
    #cierra la carga para limpiar memoria
    doc.close()
    #crea el contexto
    con = Context()
    
    vista = template.render(con)

    return HttpResponse(vista)