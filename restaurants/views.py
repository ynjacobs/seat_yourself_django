from django.shortcuts import render
from restaurants.models import Restaurant

def restaurants_list(request):
    restaurants = Restaurant.objects.all()
    context = {'restaurants': restaurants, 'title': 'Restaurants'}
    return render(request, 'index.html', context)
