from django.shortcuts import render, redirect  
from employee.forms import PizzaForm  
from employee.models import Pizza 
from employee.forms import BebidaForm
from employee.models import Bebida
# Create your views here.  
# def emp(request):  
#     if request.method == "POST":  
#         form = EmployeeForm(request.POST)  
#         if form.is_valid():  
#             try:  
#                 form.save()  
#                 return redirect('/employee/show')  
#             except:  
#                 pass  
#     else:  
#         form = EmployeeForm()  
#     return render(request,'employee/index.html',{'form':form})  
# def show(request):  
#     employees = Employee.objects.all()  
#     return render(request,"employee/show.html",{'employees':employees})  
# def edit(request, id):  
#     employee = Employee.objects.get(id=id)  
#     return render(request,'employee/edit.html', {'employee':employee})  
# def update(request, id):  
#     employee = Employee.objects.get(id=id)  
#     form = EmployeeForm(request.POST, instance = employee)  
#     if form.is_valid():  
#         form.save()  
#         return redirect("/employee/show")  
#     return render(request, 'employee/edit.html', {'employee': employee})  
# def destroy(request, id):  
#     employee = Employee.objects.get(id=id)  
#     employee.delete()  
#     return redirect("/employee/show")

def index(request) :
    return render(request,'index.html')

def cardapioIndex(request) :
    return render(request,'cardapio/index.html') 

def cardapioPizzaIndex(request) :
    pizzas = Pizza.objects.all()  
    return render(request,"cardapio/pizza/index.html",{'pizzas':pizzas}) 

def cardapioPizzaInsert(request) :
    if request.method == "POST":  
        form = PizzaForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/cardapio/pizza')  
            except:  
                pass  
    else:  
        form = PizzaForm()  
    return render(request,'cardapio/pizza/insert.html',{'form':form})  

def cardapioPizzaEdit(request,id) :
    pizza = Pizza.objects.get(id=id)  
    return render(request,'cardapio/pizza/edit.html', {'pizza':pizza})

def cardapioPizzaUpdate(request, id):  
    pizza = Pizza.objects.get(id=id)  
    form = PizzaForm(request.POST, instance = pizza)  
    if form.is_valid():  
        form.save()  
        return redirect("/cardapio/pizza")  
    return render(request, 'cardapio/pizza/edit.html', {'pizza': pizza})  

def cardapioPizzaDestroy(request, id):  
    pizza = Pizza.objects.get(id=id)  
    pizza.delete()  
    return redirect("/cardapio/pizza")

def cardapioBebidaIndex(request) :
    bebidas = Bebida.objects.all()  
    return render(request,"cardapio/bebida/index.html",{'bebidas':bebidas}) 

def cardapioBebidaInsert(request) :
    if request.method == "POST":  
        form = BebidaForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/cardapio/bebida')  
            except:  
                pass  
    else:  
        form = BebidaForm()  
    return render(request,'cardapio/bebida/insert.html',{'form':form})  

def cardapioBebidaEdit(request,id) :
    bebida = Bebida.objects.get(id=id)  
    return render(request,'cardapio/bebida/edit.html', {'bebida':bebida})

def cardapioBebidaUpdate(request, id):  
    bebida = Bebida.objects.get(id=id)  
    form = BebidaForm(request.POST, instance = bebida)  
    if form.is_valid():  
        form.save()  
        return redirect("/cardapio/bebida")  
    return render(request, 'cardapio/bebida/edit.html', {'bebida': bebida})  

def cardapioBebidaDestroy(request, id):  
    bebida = Bebida.objects.get(id=id)  
    bebida.delete()  
    return redirect("/cardapio/bebida")