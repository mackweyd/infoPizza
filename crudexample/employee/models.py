from django.db import models  
class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)  
    class Meta:  
        db_table = "employee"  

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
