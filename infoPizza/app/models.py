from django.db import models  

class Item(models.Model):   
    id = models.AutoField(primary_key=True)
    cat = models.SmallIntegerField() 
    nome = models.CharField(max_length=100)  
    desc = models.CharField(max_length=250)     
    p1 = models.DecimalField(max_digits=4,decimal_places=2)
    p2 = models.DecimalField(max_digits=4,decimal_places=2)
    p3 = models.DecimalField(max_digits=4,decimal_places=2)
    p4 = models.DecimalField(max_digits=4,decimal_places=2)  
    class Meta:  
        db_table = "item"  



class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    itens = models.ManyToManyField(Item)
    status = models.CharField(max_length=50,null=True)       
    preco =  models.DecimalField(max_digits=4,decimal_places=2,null=True) 
    metodo_pag = models.CharField(max_length=50,null=True)
    class Meta:
        db_table = "pedido"


class Mesa(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField(default=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE,null=True)
    class Meta:
        db_table = "mesa"