from django.shortcuts import render
from restaurants.models import Restaurant

def restaurants_list(request):
    restaurants = Restaurant.objects.all()
    context = {'restaurants': restaurants, 'title': 'Restaurants'}
    return render(request, 'index.html', context)

def restaurant_show(request, id):
    restaurant = Restaurant.objects.get(pk=id)
    context = {'restaurant': restaurant, 'title': restaurant.name}
    return render(request, 'restaurant_details.html', context)
