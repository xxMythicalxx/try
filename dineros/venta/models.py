from django.db import models

# Create your models here.
class tipo_pago(models.Model):
    nom_tip_pag = models.TextField(max_length=10)
    
class tipo_usuario(models.Model):
    nom_tip_usu = models.TextField(max_length=10) 
    
class genero(models.Model):
    nom_gen = models.TextField(max_length=10) 
    
class tipo_reseña(models.Model):
    nom_tip_res = models.TextField(max_length=10) 

class usuario(models.Model):
    genero = models.ForeignKey(genero, on_delete=models.CASCADE)
    tipo_usuario = models.ForeignKey(tipo_usuario, on_delete=models.CASCADE)
    nom_usu = models.TextField(max_length=30)
    ape_usu = models.TextField(max_length=30)
    corre_usu = models.TextField(max_length=50)
    rut_usu = models.TextField(max_length=12)
    num_usu = models.TextField(max_length=12)
    des_usu = models.TextField(max_length=100)
    est_prem = models.BooleanField(False)
    fec_res = models.DateTimeField()
    
class reseña(models.Model):
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    tipo_reseña = models.ForeignKey(tipo_reseña, on_delete=models.CASCADE)
    des_res = models.TextField(max_length=50)
    fec_res = models.DateTimeField()
    
class buscar(models.Model):
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)

class publicacion(models.Model):
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    buscar = models.ForeignKey(buscar, on_delete=models.CASCADE)
    reseña = models.ForeignKey(reseña, on_delete=models.CASCADE)
    tit_pub = models.TextField(max_length=50)
    fec_pub = models.DateTimeField()
    des_pub = models.TextField(max_length=100)
    
class contactar(models.Model):
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    buscar = models.ForeignKey(buscar, on_delete=models.CASCADE)
    con = models.TextField(max_length=50)
    fec_con = models.DateTimeField()
    
class acuerdo(models.Model):
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    contactar = models.ForeignKey(contactar, on_delete=models.CASCADE)
    fec_acu = models.DateTimeField()
    des_acu = models.TextField(max_length=100)
    
class transferencia(models.Model):
    tipo_pago = models.ForeignKey(tipo_pago, on_delete=models.CASCADE)
    acuerdo = models.ForeignKey(acuerdo, on_delete=models.CASCADE)
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    mon = models.IntegerField()
    fec_mon = models.DateTimeField()