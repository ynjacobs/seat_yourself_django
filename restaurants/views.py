from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
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
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    form = ReservationForm(request.POST)
    reservation = form.instance
    reservation.restaurant = restaurant
    reservation.user = User.objects.all()[0]
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('restaurant_show', args=[restaurant.pk]))
    else:
        context = {'restaurant': restaurant, 'reservation_form': form, 'title': restaurant.name}
        return render(request, 'restaurant_details.html', context)
