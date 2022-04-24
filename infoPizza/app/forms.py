from django import forms  
from app.models import *  
class PizzaForm(forms.ModelForm):  
    class Meta:  
        model = Pizza  
        fields = "__all__"  
class BebidaForm(forms.ModelForm):  
    class Meta:  
        model = Bebida  
        fields = "__all__"  
class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = "__all__"
class ItensPedidoForm(forms.ModelForm):
    class Meta:
        model = ItensPedido
        fields = "__all__"
class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = "__all__"