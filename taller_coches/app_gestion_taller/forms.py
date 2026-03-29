#Mis formularios
from django import forms
from .models import Cliente, Coche, Servicio, CocheServicio

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__' #Con esto se genera la tabal entera (de Cliente en este ejemplo)

class CocheForm(forms.ModelForm):
    class Meta:
        model = Coche
        fields = '__all__'

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'

class CocheServicioForm(forms.ModelForm):
    class Meta:
        model = CocheServicio
        fields = '__all__'