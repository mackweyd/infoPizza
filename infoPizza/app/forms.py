from django import forms  
from app.models import *  

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = "__all__"
class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = "__all__"