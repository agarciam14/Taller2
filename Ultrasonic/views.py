from django.shortcuts import render, HttpResponse
import requests

def Ultrasonic(request):
    # Verifica si hay un parámetro distance en la petición GET
    if 'distance' in request.GET:
        distance = request.GET['distance']
        lat = request.GET['lat']
        lng = request.GET['lng']
        area = request.GET['area']
        # Verifica si el distance no esta vacio
        if distance:
            # Crea el json para realizar la petición POST al Web Service
            args = {'distance': distance, 'lat': lat, 'lng': lng, 'area':area}
            response = requests.post('http://127.0.0.1:8000/ultrasonics/', args)
            # Convierte la respuesta en JSON
            Ultrasonic_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://127.0.0.1:8000/ultrasonics/')
    # Convierte la respuesta en JSON
    ultrasonics = response.json()
    # Rederiza la respuesta en el template Ultrasonic
    return render(request, "Ultrasonic/Ultrasonic.html", {'ultrasonics': ultrasonics})
