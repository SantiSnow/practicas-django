from django.http import HttpResponse

#views
def index(httpRequest):
    return HttpResponse("Bienvenido al index de la aplicacion.")