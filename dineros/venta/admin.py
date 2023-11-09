from django.contrib import admin

# Register your models here.
from venta.models import usuario,reseña,publicacion,buscar,contactar,acuerdo,transferencia,tipo_pago,tipo_usuario,genero,tipo_reseña

class usuarioadmin(admin.ModelAdmin):
    list_display = ['id','nom_usu','ape_usu','corre_usu','rut_usu','num_usu','des_usu','est_prem','fec_res','genero_id','tipo_usuario_id']
    
class transferenciaadmin(admin.ModelAdmin):
    list_display = ['id',	'mon',	'fec_mon',	'acuerdo_id',	'tipo_pago_id',	'usuario_id']
    
class tipo_usuarioadmin(admin.ModelAdmin):
    list_display = ['id',	'nom_tip_usu']
    
class tipo_reseñaadmin(admin.ModelAdmin):
    list_display = ['id',	'nom_tip_res']
    
class tipo_pagoadmin(admin.ModelAdmin):
    list_display = ['id',	'nom_tip_pag']
    
class reseñaadmin(admin.ModelAdmin):
    list_display = ['id',	'des_res',	'fec_res',	'tipo_reseña_id',	'usuario_id']

class publicacionadmin(admin.ModelAdmin):
    list_display = [	'id',	'tit_pub',	'fec_pub',	'des_pub',	'buscar_id',	'reseña_id',	'usuario_id'	]

class generoadmin(admin.ModelAdmin):
    list_display = ['id',	'nom_gen']
    
class contactaradmin(admin.ModelAdmin):
    list_display = ['id',	'con',	'fec_con',	'buscar_id',	'usuario_id'	]

class buscaradmin(admin.ModelAdmin):
    list_display = ['id',	'usuario_id']
    
class acuerdoadmin(admin.ModelAdmin):
    list_display = ['id',	'fec_acu',	'des_acu',	'contactar_id',	'usuario_id']

admin.site.register(usuario, usuarioadmin)
admin.site.register(transferencia, transferenciaadmin)
admin.site.register(tipo_usuario, tipo_usuarioadmin)
admin.site.register(tipo_reseña, tipo_reseñaadmin)
admin.site.register(tipo_pago, tipo_pagoadmin)
admin.site.register(reseña, reseñaadmin)
admin.site.register(publicacion, publicacionadmin)
admin.site.register(genero, generoadmin)
admin.site.register(contactar, contactaradmin)
admin.site.register(buscar, buscaradmin)
admin.site.register(acuerdo, acuerdoadmin)


















