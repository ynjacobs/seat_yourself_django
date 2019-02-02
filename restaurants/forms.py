from django.forms import ModelForm, DateTimeField
from restaurants.models import Reservation

class ReservationForm(ModelForm):

    class Meta:
        model = Reservation
        fields = ['party_size', 'datetime', 'notes']