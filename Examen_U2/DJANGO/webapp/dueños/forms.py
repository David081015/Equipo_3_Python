from django.forms import ModelForm
from dueños.models import Dueño

class Dueñoform(ModelForm):
    class Meta:
        model = Dueño
        fields = '__all__'