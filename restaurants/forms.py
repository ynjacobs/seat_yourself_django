from datetime import date
from django.forms import ModelForm, TimeInput, DateInput
from restaurants.models import Reservation

class ReservationForm(ModelForm):

    class Meta:
        model = Reservation
        fields = ['party_size', 'date', 'time', 'notes']
        widgets = {
            'time': TimeInput(attrs={'type': 'time' }),
            'date': DateInput(attrs={'type': 'date', 'min': date.today() })
        }
