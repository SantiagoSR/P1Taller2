from django.shortcuts import render
from django.shortcuts import render, HttpResponse
import requests
def luminosity(request):
    # Verifica si hay un parámetro value en la petición GET
    if 'value' in request.GET:
        value = request.GET['value']
        latitude = request.GET['latitude']
        lenght = request.GET['lenght']
        terrain = request.GET['terrain']
        # Verifica si el value no esta vacio
        if value:
            # Crea el json para realizar la petición POST al Web Service
            args = {'type': 'lux', 'value': value, 'latitude': latitude, 'lenght': lenght, 'terrain': terrain}
            #response = requests.post('http://127.0.0.1:8000/luminosity/', args)
            response = requests.post('https://p1-eafit-ssantacrur.azurewebsites.net/', args)
            # Convierte la respuesta en JSON
            luminosity_json = response.json()

    # Realiza una petición GET al Web Services
    #response = requests.get('http://127.0.0.1:8000/luminosity/')
    response = requests.get('https://p1-eafit-ssantacrur.azurewebsites.net/')
    # Convierte la respuesta en JSON
    luminosity = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "luminosity/luminosity.html", {'luminosity': luminosity})

# Create your views here.
