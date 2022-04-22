from django import forms  
from employee.models import Employee
from employee.models import Pizza  
class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__"  
class PizzaForm(forms.ModelForm):  
    class Meta:  
        model = Pizza  
        fields = "__all__"  