from django.shortcuts import render
from restaurants.forms import ReservationForm
from restaurants.models import Restaurant

def restaurants_list(request):
    restaurants = Restaurant.objects.all()
    context = {'restaurants': restaurants, 'title': 'Restaurants'}
    return render(request, 'index.html', context)

def restaurant_show(request, id):
    restaurant = Restaurant.objects.get(pk=id)
    form = ReservationForm()
    context = {'restaurant': restaurant, 'reservation_form': form, 'title': restaurant.name}
    return render(request, 'restaurant_details.html', context)

def reservation_create(request, restaurant_id):
    pass
