from django.shortcuts import render
from car_model.models import CarModel, Brand

def home(request):
    cars = CarModel.objects.all()
    brand = Brand.objects.all()
    return render(request, 'home.html', {'cars': cars, 'brand': brand})