from django import forms  
from employee.models import Employee
from employee.models import Pizza
from employee.models import Bebida  
class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__"  
class PizzaForm(forms.ModelForm):  
    class Meta:  
        model = Pizza  
        fields = "__all__"  
class BebidaForm(forms.ModelForm):  
    class Meta:  
        model = Bebida  
        fields = "__all__"  