from django.db import models  

class Pizza(models.Model):   
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)  
    desc = models.CharField(max_length=250)  
    p1 = models.DecimalField(max_digits=4,decimal_places=2)
    p2 = models.DecimalField(max_digits=4,decimal_places=2)
    p3 = models.DecimalField(max_digits=4,decimal_places=2)
    p4 = models.DecimalField(max_digits=4,decimal_places=2)  
    class Meta:  
        db_table = "pizza"  

class Bebida(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    p1 = models.DecimalField(max_digits=4,decimal_places=2)
    p2 = models.DecimalField(max_digits=4,decimal_places=2)
    p3 = models.DecimalField(max_digits=4,decimal_places=2)
    p4 = models.DecimalField(max_digits=4,decimal_places=2)
    class Meta:
        db_table = "bebida"

class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=50)
    preco =  models.DecimalField(max_digits=4,decimal_places=2)
    metodo_pag = models.CharField(max_length=50)
    class Meta:
        db_table = "pedido"

class ItensPedido(models.Model):
    id = models.OneToOneField(Pedido,on_delete=models.CASCADE,primary_key=True)
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=4,decimal_places=2)
    class Meta:
        db_table = "itensPedido"

class Mesa(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField()
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    class Meta:
        db_table = "mesa"