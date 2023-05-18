from django import forms
from .models import Presa

class notaForm(forms.ModelForm):
    class Meta:
        model=Presa
        fields='__all__'
