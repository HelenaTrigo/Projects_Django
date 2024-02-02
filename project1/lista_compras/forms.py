
from django import forms

from lista_compras.models import Artigo


class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = "__all__"