from django.shortcuts import render, HttpResponse

def Ultrasonic(request):
    return render(request, "Ultrasonic/Ultrasonic.html")
