from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, reverse, redirect
from restaurants.forms import ReservationForm, LoginForm
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
    reservation.user = request.user
    if form.is_valid():
        form.save()
        return redirect(reverse('restaurant_show', args=[restaurant.pk]))
    else:
        context = {'restaurant': restaurant, 'reservation_form': form, 'title': restaurant.name}
        return render(request, 'restaurant_details.html', context)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            user = authenticate(username=username, password=pw)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('home'))
                else:
                    form.add_error('username', 'This account has been disabled')
                    context = {'form': form}
                    return render(request, 'login.html', context)
            else:
                form.add_error('username', 'Login failed')
                context = {'form': form}
                return render(request, 'login.html', context)
    else:
        form = LoginForm()
        context = {'form': form}
        return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect(reverse('home'))
