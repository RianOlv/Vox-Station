from django.shortcuts import render


def InicioView(request):
    return render(request, './inicio/index.html')
