# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

    


class Inventario(models.Model):
    
    id = models.AutoField(primary_key=True,unique=True)
    cn = models.TextField(blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)
    pvf = models.TextField(blank=True, null=True)
    pvp = models.TextField(blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    zonap = models.ForeignKey ('fichas.Zona',verbose_name='Zona de aplicación',on_delete=models.SET_NULL,null=True,blank=True)
    indicaciones = models.ManyToManyField('fichas.Indicacion',blank=True, related_name="indicacionlist")
    puntuacion = models.ManyToManyField('fichas.Puntuar',blank=True)
    media = models.DecimalField(max_digits=4,decimal_places=2,null=True,blank=True)

    def __str__(self):
        return self.nombre 
    
    class Meta:
        managed = True
        db_table = 'Inventario'
        
    def save(self, *args, **kwargs):
        listanotas=[]
        if self.puntuacion.all():
            for puntuacion in self.puntuacion.all():
                listanotas.append(puntuacion.nota)
            
            mediatotal= sum(listanotas)/len(listanotas)
            self.media=round(mediatotal,2)
            super().save(*args, **kwargs)
        else:
         super().save(*args, **kwargs)
            
        
            
    
        

    
    
    
    
def zona_upload_to(instance, filename):
    old_instance = Zona.objects.get(pk=instance.pk)
    old_instance.image.delete()
    return 'zonas/' + filename   

class Zona(models.Model):
    nombre= models.CharField(max_length=30)
    image= models.ImageField(upload_to=zona_upload_to,blank=True, null=True)
    
    def __str__(self):
        return self.nombre
    class Meta:
        managed = True
        app_label='fichas'
        ordering= ('nombre',)

class Indicacion(models.Model):
    nombre= models.CharField(max_length=40)
    zona= models.ManyToManyField('fichas.Zona')
    def __str__(self):
        return self.nombre
    class Meta:
        managed = True
        app_label='fichas' 
        ordering= ('nombre',)
   
    
class Puntuar(models.Model):
    dni=models.CharField(max_length=9,blank=True,null=True,help_text='12345678A')
    nota=models.DecimalField(max_digits=4,decimal_places=2)
    fecha=models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return  '({}) {}/{}/{}'.format(self.dni,self.fecha.day, self.fecha.month, self.fecha.year)