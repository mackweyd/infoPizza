from django.shortcuts import render, redirect  
from employee.forms import EmployeeForm
from employee.forms import PizzaForm  
from employee.models import Employee 
from employee.models import Pizza 
# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/employee/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'employee/index.html',{'form':form})  
def show(request):  
    employees = Employee.objects.all()  
    return render(request,"employee/show.html",{'employees':employees})  
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'employee/edit.html', {'employee':employee})  
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/employee/show")  
    return render(request, 'employee/edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/employee/show")

def index(request) :
    return render(request,'index.html') 

def cardapioIndex(request) :
    pizzas = Pizza.objects.all()  
    return render(request,"cardapio/index.html",{'pizzas':pizzas}) 

def insert(request) :
    if request.method == "POST":  
        form = PizzaForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/cardapio/index.html')  
            except:  
                pass  
    else:  
        form = PizzaForm()  
    return render(request,'cardapio/insert.html',{'form':form})  

def cardapioEdit(request,id) :
    pizza = Pizza.objects.get(id=id)  
    return render(request,'cardapio/edit.html', {'pizza':pizza})

def cardapioUpdate(request, id):  
    pizza = Pizza.objects.get(id=id)  
    form = PizzaForm(request.POST, instance = pizza)  
    if form.is_valid():  
        form.save()  
        return redirect("/cardapio/index.html")  
    return render(request, 'cardapio/edit.html', {'pizza': pizza})  

def cardapioDestroy(request, id):  
    pizza = Pizza.objects.get(id=id)  
    pizza.delete()  
    return redirect("/cardapio/index.html")