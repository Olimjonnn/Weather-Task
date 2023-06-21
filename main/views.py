from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from main.serializers import InfoSerilizer
import requests, json
from rest_framework import generics
from main.models import *
from rest_framework import permissions
# from django.contrib.gis.geoip import GeoIP
import requests


BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "62cd9fd62c871f7168c8205d2a3504be"

class InfoView(generics.ListAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerilizer
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        ip = requests.get('https://api.ipify.org?format=json')
        ip_data = json.loads(ip.text)
        res = requests.get('http://ip-api.com/json/'+ip_data['ip'])
        location_data_one = res.text
        location_data = json.loads(location_data_one)
        city = location_data['city']
        user = request.user
        URL = BASE_URL + "q=" + city + "&appid=" + API_KEY
        response = requests.get(URL)
        dat = []
        if response.status_code == 200:
            data = response.json()
            main = data['main']
            temperature = float(main['temp'])
            humidity = main['humidity']
            pressure = main['pressure']
            report = data['weather']
            Data = {
                f"City name: {city}",
                f"Temperature: {int(temperature-273.15)}",
                f"Humidity: {humidity}",
                f"Pressure: {pressure}",
                f"Weather Report: {report[0]['description']}",
            }
            dat.append(Data)
            return Response(dat)
        else:
            return("Error in the HTTP request")


BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
REGIONS = ['Tashkent', 'Andijon', "Samarqand", "Buxoro", "Farg'ona", 'Namangan', 'Xiva', 'Jizzax']
API_KEY = "62cd9fd62c871f7168c8205d2a3504be"

class InfoWeather(APIView):
    pass
class InfooView(APIView):
    def get(self, request):
        city = request.GET.get('city')
        results = {"City name":[], 'Information':[]}
        for region in REGIONS:
            URL = BASE_URL + "q=" + str(region) + "&appid=" + API_KEY
            response = requests.get(URL)
            
            if response.status_code == 200:
                data = response.json()
                main = data['main']
                temperature = float(main['temp'])
                humidity = main['humidity']
                pressure = main['pressure']
                report = data['weather']
                Data = {
                    f"City: {region}",
                    f"Temperature: {int(temperature - 273.15)}",
                    f"Humidity: {humidity}",
                    f"Pressure: {pressure}",
                    f"Weather Report: {report[0]['description']}",
                }
                # results.append(Data)
                results['City name'].append(region)
                results['Information'].append(Data)
        return Response(results) # Insert actual Response Class