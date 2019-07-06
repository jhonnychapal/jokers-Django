from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_Cliente = models.CharField(max_length=50, primary_key=True)
    nom_Cliente = models.CharField(max_length=50)
    dir_Cliente = models.CharField(max_length=50)
    ciu_Cliente = models.CharField(max_length=50)
    tel_Cliente = models.CharField(max_length=20)

    def __str__(self):
        return (self.nom_Cliente)

class Factura(models.Model):
    no_Factura = models.CharField(max_length=50, primary_key=True)
    cliente = models.ForeignKey(Cliente, null=True, blank=True,on_delete=models.PROTECT)
    fech_Factura = models.DateField(auto_now_add=True)
    subtotal = models.DecimalField(max_digits=15,decimal_places=2)
    iva = models.DecimalField(max_digits=15,decimal_places=2)
    total = models.DecimalField(max_digits=15,decimal_places=2)

    def __str__(self):
        return(self.no_Factura)

class Articulo(models.Model):
    id_Articulo = models.CharField(max_length=50, primary_key=True)
    nom_Articulo = models.CharField(max_length=50)
    vr_Unitario = models.DecimalField(max_digits=15,decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return(self.nom_Articulo)

class Detalle(models.Model):
    articulo = models.ForeignKey(Articulo,null=True, blank=True,on_delete=models.PROTECT)
    factura = models.ForeignKey(Factura,null=True,blank=True,on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    total_Detalle = models.DecimalField(max_digits=15,decimal_places=2)

    def __str__(self):
        return(str(self.articulo) + "  " + str(self.cantidad))

    
class Proveedor(models.Model):
    nit_Proveedor = models.CharField(max_length=50, primary_key=True)
    nom_Proveedor = models.CharField(max_length=50)
    dir_proveedor = models.CharField(max_length=50)
    ciu_proveedor = models.CharField(max_length=50)
    tel_proveedor = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return(self.nom_Proveedor + "  " + self.ciu_proveedor + "  " + self.tel_proveedor)

class Compra(models.Model):
    no_compra = models.CharField(max_length=20, primary_key=True)
    proveedor = models.ForeignKey(Proveedor, null=True, blank=True,on_delete=models.PROTECT)
    fech_Compra = models.DateField(auto_now_add=True)
    num_factura = models.CharField(max_length=20)
    articulo = models.ManyToManyField(Articulo)
    cantidad = models.IntegerField()

    def __str__(self):
        return(self.no_compra)
