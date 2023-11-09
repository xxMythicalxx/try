
from django.shortcuts import render

from venta.models import usuario 

from datetime import datetime

from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse

import logging

# Create your views here.
@csrf_exempt
def register(request):
    if request.method == "POST":
        ema = request.POST["ema"]
        nom = request.POST["nom"]
        ape = request.POST["ape"]
        tip = request.POST["tip"]
        pas = request.POST["pas"]

        if (tip == "Buscador (Para encontrar oficios)"):
            tip = 1
        elif (tip =="Promotor (Para ofrecer oficios)"):
             tip = 2

        if (ema != ''or nom != ''or ape != ''or pas != ''):
            check = usuario.objects.filter(nom_usu=nom).values()
            if check:
                pass
            else:
                usu = usuario(genero_id =1,tipo_usuario_id = tip,nom_usu = nom,ape_usu = ape,corre_usu = ema,rut_usu = 00,num_usu=pas,des_usu=00,est_prem=False,fec_res=datetime.now())
                usu.save()
                return HttpResponse("hola uwu")

    else:
            dato = {'r2' : 'No se puede acceder por URL'}

@csrf_exempt
def login(request):
     if request.method == "POST":
            ema = request.POST["ema"]
            pas = request.POST["pas"]

            check = usuario.objects.filter(corre_usu=ema,num_usu=pas).values()
            if check:
                check2 =usuario.objects.filter(corre_usu=ema,num_usu=pas,tipo_usuario_id = 1).values()
                request.session['status'] = True
                request.session['ema'] = ema
                if (check2):
                    return HttpResponse("publica")
                else:
                    return HttpResponse("notpublica")
                
                
@csrf_exempt
def getusu(request):
   ##check = request.session.get('status')
    ##if check is True:
        ema = request.session.get('ema') 
        usu = usuario.objects.get(corre_usu="nocreo")
        mail = str(usu.corre_usu)
        return HttpResponse(mail)
        
