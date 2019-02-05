from django.shortcuts import render
from fichas.models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

@login_required(login_url='admin:login')
def buscar(request,*args,**kwargs):
    fichas = Inventario.objects.all()
    zonas = []
    
    for ficha in fichas:
        if ficha.zonap is not None:
            if ficha.zonap not in zonas: 
                zonas.append(ficha.zonap.id)

    zonasf=Zona.objects.filter(pk__in=zonas)    
        
        
        
           
            
       
    return render(request,"fastsearch/buscar.html",{'zonas':zonasf})
    
                

@login_required(login_url='admin:login')
def buscarzona(request,id,*args,**kwargs):
    fichas = Inventario.objects.all()
    zonaid = id
    zonasficha=[]
    indicaciones=[]
    zonas= Zona.objects.filter(id=zonaid)
    for zona in zonas:
        nombre= zona.nombre
        

        
    for ficha in fichas:
        if ficha.zonap_id == zonaid:
            zonasficha.append(ficha)

    if request.method=='GET':
        
            

        for ficha in zonasficha:
            for indicacion in ficha.indicaciones.all():
                if indicacion not in indicaciones:
                    indicaciones.append(indicacion)
        return render(request,"fastsearch/buscarzona.html",{'indicaciones':indicaciones,'nombre':nombre})
            




    if request.method== 'POST':
        
        indicaciones_elegidas=[]
        print(indicaciones_elegidas)
        fichasfinal=[]
        dic= request.POST
        for a in dic:
            if dic[a] == 'on':
                indicaciones_elegidas.append(a)
        print (indicaciones_elegidas)
        
        
        if len(indicaciones_elegidas)== 0:
            fichasfinal=zonasficha
        else:
            for ficha in zonasficha:
                indicacionesficha=ficha.indicaciones.all()
                nombreindicacionesficha=[]
                #HACER LISTA CON SOLO LOS NOMBRES  DE LAS INDICACIONES DE LA FICHA
                for a in indicacionesficha:
                    print(a)
                    nombreindicacionesficha.append(a.nombre)
                #------------------------------------------------------
                
                c=0
                longitud=len(indicaciones_elegidas)
                for indicacion in indicaciones_elegidas:
                        
                        if indicacion in nombreindicacionesficha:
                            c=c+1
                if c==longitud:
                    fichasfinal.append(ficha)            
        fichas_ids=[]
        for ficha in fichasfinal:
            fichas_ids.append(ficha.id)
        fichasfinalpuntuacion=Inventario.objects.filter(pk__in=fichas_ids).order_by('-media')

                        
                        
                    
                            
                        
        return render (request,"fastsearch/fichasfinal.html",{'fichasfinal':fichasfinalpuntuacion})
            
            
        
    
        

