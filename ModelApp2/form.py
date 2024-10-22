from django import forms
from ModelApp2.models import tienda
class formTienda(forms.ModelForm):
    class Meta:
        model=tienda
        fields='__all__'