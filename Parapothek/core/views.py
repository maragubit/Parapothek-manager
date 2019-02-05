from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator






# Create your views here.

    

@login_required(login_url='admin:login')
def home(request):
    return render(request,"core/portada.html")
   















    
    
        
            


    



    
    


    