from django.shortcuts import render, redirect  
from app.forms import * 
from app.models import *

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

def pedidosIndex(request) :
    mesas = Mesa.objects.all
    return render(request,'pedidos/index.html',{'mesas':mesas}) 
    
def pedidosMesaOrder(request,id) :
    if request.method == "POST":  
        form = ItensPedidoForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/pedidos')  
            except:  
                pass  
    else:  
        form = ItensPedidoForm 
        pedidonovo = Pedido()
        pedidonovo.save()
        form(initial={'id':pedidonovo.id})
        mesa = Mesa.objects.get(id=id)
        mesa() = pedidonovo.id
        mesa.save()        
    return render(request,'pedidos/mesa/order.html',{'form':form})

def caixaMesaInsert(request) :
    Mesa.objects.create()
    return redirect('/pedidos')
  
