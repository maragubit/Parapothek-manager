from django.shortcuts import render
from django.urls import reverse_lazy
from . import views
from .models import *
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .forms import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



# Create your views here.
@login_required(login_url='admin:login')
def buscadorfichas(request):
    if request.method=='POST':
        data=request.POST.get("buscar")
        objectlist=Inventario.objects.filter(nombre__icontains=data)| Inventario.objects.filter(cn__icontains=data)
        return render(request,"fichas/buscadorfichas.html",{'objectlist':objectlist,})
    else:
        objectlist=Inventario.objects.all()
        return render(request,"fichas/buscadorfichas.html",{'objectlist':objectlist,}) 
    


#-----------------Modelo ficha-------------------------------
@method_decorator(login_required(login_url='admin:login'), name='dispatch')
class FichasViews(ListView):
    model = Inventario
    template_name = "fichas/fichas.html"
    paginate_by = 30
@method_decorator(login_required(login_url='admin:login'), name='dispatch')
class FichasViewsPuntuacion(ListView):
    model = Inventario
    template_name = "fichas/fichaspuntuacion.html"
    

    def get_queryset(self):
        fichaspuntuadas=[]
        fichas= Inventario.objects.filter(media__gte=7).order_by('-media')
        
       
        
        self.queryset = fichas
        return self.queryset

@method_decorator(login_required(login_url='admin:login'), name='dispatch')    
class FichaUpdate(UpdateView):
    model = Inventario
    template_name = "fichas/editarficha.html"
    fields= ('zonap',)
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        listapuntuaciones = []
        
        puntuaciones= self.object.puntuacion.all()
        for puntuacion in puntuaciones:
            listapuntuaciones.append(puntuacion.nota)
        if len(listapuntuaciones)== 0:
            votos=0
            imagen='core/assets/img/0stars.png'
            context['votos']=votos
            context['imagen']=imagen
            return context
        else:
            if self.object.media is None:
                imagen='core/assets/img/0stars.png'
                votos=len(listapuntuaciones)
                context['votos']=votos
                context['imagen']=imagen
                return context
            
            elif self.object.media >= 9.51:
                imagen='core/assets/img/5stars.png'
                votos=len(listapuntuaciones)
                context['votos']=votos
                context['imagen']=imagen
                return context
                
            elif self.object.media > 7.51 and self.object.media <=9.50 : 
                imagen='core/assets/img/4stars.png'
                votos=len(listapuntuaciones)
                context['votos']=votos
                context['imagen']=imagen
                return context 
            elif self.object.media > 5.50 and self.object.media <=7.50 :  
                imagen='core/assets/img/3stars.png'
                votos=len(listapuntuaciones)
                context['votos']=votos
                context['imagen']=imagen
                return context
            elif self.object.media > 3.51 and self.object.media <=5.50 :   
                imagen='core/assets/img/2stars.png'
                votos=len(listapuntuaciones)
                context['votos']=votos
                context['imagen']=imagen
                return context
            elif self.object.media > 1.51 and self.object.media <=3.50:
                imagen='core/assets/img/1stars.png.jpg'
                votos=len(listapuntuaciones)
                context['votos']=votos
                context['imagen']=imagen
                return context
            else:
                imagen='core/assets/img/0stars.png'
                votos=len(listapuntuaciones)
                context['votos']=votos
                context['imagen']=imagen
                return context
   
    def get_success_url(self):
        return reverse_lazy('fichaupdate', args=[self.object.id]) + '?ok'




#-----------------Modelo ZonaAplicacion---------------------------------------------------------------------

# Ver lista Zonas de aplicación:
@method_decorator(login_required(login_url='admin:login'), name='dispatch')
class ZonasViews(ListView):
    model = Zona
    template_name = "fichas/zonasaplicacion.html"

#Crear zona de aplicación
@method_decorator(login_required(login_url='admin:login'), name='dispatch')
class ZonaCreate(CreateView):
    template_name = "fichas/crearzona.html"
    model = Zona
    fields = "__all__"
    def get_success_url(self):
        return reverse_lazy('zonacreate') + '?ok'

# Editar ZonaAplicaion
@method_decorator(login_required(login_url='admin:login'), name='dispatch')
class ZonaUpdate(UpdateView):
    model = Zona
    template_name = "fichas/editarzona.html"
    fields ="__all__"
    def get_success_url(self):
        return reverse_lazy('zonaupdate', args=[self.object.id]) + '?ok'

# Borrar Zona de Aplicación
@method_decorator(login_required(login_url='admin:login'), name='dispatch')
class ZonaDelete(DeleteView):
    model = Zona
    template_name = "fichas/borrarzona.html"
    success_url = reverse_lazy('zonas')


#-----------------Modelo Indicaciones---------------------------------------------------------------------
@method_decorator(login_required(login_url='admin:login'), name='dispatch')
class IndicacionesViews(ListView):
    model = Indicacion
    template_name = "fichas/indicaciones.html"
@method_decorator(login_required(login_url='admin:login'), name='dispatch')
class IndicacionCreate(CreateView):
    template_name = "fichas/crearindicacion.html"
    model = Indicacion
    form_class = IndicacionesForm
    def get_success_url(self):
        return reverse_lazy('indicacioncreate') + '?ok'
@method_decorator(login_required(login_url='admin:login'), name='dispatch')
class IndicacionUpdate(UpdateView):
    model = Indicacion
    template_name = "fichas/editarindicacion.html"
    form_class = IndicacionesForm
    def get_success_url(self):
        return reverse_lazy('indicacionupdate', args=[self.object.id]) + '?ok'
@method_decorator(login_required(login_url='admin:login'), name='dispatch')
class IndicacionDelete(DeleteView):
    model = Indicacion
    template_name = "fichas/borrarindicacion.html"
    success_url = reverse_lazy('indicaciones')
@login_required(login_url='admin:login')
def puntuar(request,id,*args,**kwargs):
    fichaid= id
    
    ficha= Inventario.objects.get(id=fichaid) #ya tenemos el objeto para la foreign key.
    from .forms import PuntuarForm
    form = PuntuarForm()
    nombre= ficha.nombre


    if request.method=='POST':
        dni= request.POST ['dni']
        nota= request.POST ['nota']
        from .models import Puntuar
        
        if len(dni)== 9 and float(nota) <= 10:
            comprobante=0
            a=Puntuar.objects.create(dni=dni,nota=nota)
            for puntuacion in ficha.puntuacion.all():
                if puntuacion.dni == a.dni:
                    comprobante += 1
                

            if comprobante == 0:
                a.save()
                ficha.puntuacion.add(a)
                ficha.save()
                listanotas=[]
                for nota in ficha.puntuacion.all():
                    listanotas.append(nota.nota)
                
               
                
                respuesta1='Nueva puntuacion añadida!!!!!!'
                
                return render(request,"fichas/puntuar.html",{'nombre':nombre,"respuesta1":respuesta1,'fichaid':fichaid,'form':form,})



            else:
                respuesta2=' {} ya ha votado anteriormente este producto!!!'.format(dni)
                return render(request,"fichas/puntuar.html",{'nombre':nombre,"respuesta2":respuesta2,'fichaid':fichaid,'form':form})
        
        else:
            respuesta2= 'Error al introducir los datos'
            return render(request,"fichas/puntuar.html",{'nombre':nombre,'form':form,'respuesta2':respuesta2,'fichaid':fichaid})
            
            
    return render(request,"fichas/puntuar.html",{'nombre':nombre,'form':form,'fichaid':fichaid})

@login_required(login_url='admin:login')
def indicacioneschoose(request,*args,**kwargs):
    from .models import Inventario,Indicacion
    from .forms import InventarioIndicacionesForm
    fichapk= kwargs['pk']
    ficha= Inventario.objects.get( pk=fichapk ) #ficha seleccionada. ahora hay que seleccionar la zona.
    zona= ficha.zonap
    indicaciones=Indicacion.objects.filter(zona=zona)
    form=InventarioIndicacionesForm(instance=ficha)
    form.fields["indicaciones"].queryset = indicaciones
    if request.method == "POST":
        form=InventarioIndicacionesForm(request.POST)
        
        if form.is_valid():
            respuesta='Indicaciones incluidas'

            for indicacion in form.cleaned_data['indicaciones']:
                ficha.indicaciones.add(indicacion)
                ficha.save()
            form.fields["indicaciones"].queryset = indicaciones
            
            
            
            
            
            
            return render(request,"fichas/indicacioneschoose.html",{'ficha':ficha,'respuesta':respuesta,'form':form,'fichaid':fichapk})
        else:
            respuesta='Error en el formulario!'
            return render(request,"fichas/indicacioneschoose.html",{'ficha':ficha,'respuesta':respuesta,'form':form,'fichaid':fichapk})
    respuesta=''
    return render(request,"fichas/indicacioneschoose.html",{'ficha':ficha,'form':form,'respuesta':respuesta,'fichaid':fichapk})

    

