from django.http import HttpResponse
import datetime

#views
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