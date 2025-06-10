from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')  # asegúrate de que el archivo 'inicio.html' exista en tus templates

