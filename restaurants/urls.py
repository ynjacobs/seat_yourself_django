from django.urls import path
import restaurants.views as views

urlpatterns = [
    path('', views.restaurants_list, name='restaurants_list'),
]
