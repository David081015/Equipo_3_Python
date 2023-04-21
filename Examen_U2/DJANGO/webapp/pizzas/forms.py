from django.forms import ModelForm
from pizzas.models import Pizza

class Pizzaform(ModelForm):
    class Meta:
        model = Pizza
        fields = '__all__'