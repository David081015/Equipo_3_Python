from django.forms import ModelForm
from repartidores.models import Repartidor

class Repartidorform(ModelForm):
    class Meta:
        model = Repartidor
        fields = '__all__'