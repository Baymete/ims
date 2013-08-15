from django.http import HttpResponse

def route(request):
    return HttpResponse("hola")