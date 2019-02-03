from django.urls import path
import restaurants.views as views

urlpatterns = [
    path('restaurants/', views.restaurants_list, name='restaurants_list'),
    path('restaurants/<int:id>/', views.restaurant_show, name='restaurant_show'),
    path('restaurants/<int:restaurant_id>/reservations/create/', views.reservation_create, name='reservation_create'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]
