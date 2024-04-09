from django import forms
from .models import Proveedor, Producto

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'apellido', 'dni']

class ProductoForm(forms.ModelForm):
    proveedor = forms.ModelChoiceField(queryset=None)
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock', 'proveedor']
        widgets = {
            'proveedor': forms.Select()
        }

    def __init__(self, *args, **kwargs):
        initial_proveedor_choices = kwargs.pop('proveedor_choices', None)  # Obtener proveedor_choices del kwargs
        super().__init__(*args, **kwargs)
        if initial_proveedor_choices is not None:
            self.fields['proveedor'].queryset = initial_proveedor_choices