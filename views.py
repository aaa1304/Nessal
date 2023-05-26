
from django.shortcuts import render

from .forms import Contactforms
# Create your views here.



def index(request):
  if request.method == "POST" :        
    contact = Contactforms(request.POST)
    if contact.is_valid:
       contact.save()

  
  context = {
     'Contactforms': Contactforms(),
  }

  return render(request, 'pages/index.html' , context)