from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.template import loader
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def index(request):
    if request.method == 'POST' :
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added')
            return redirect('index')
        else:
            messages.error(request, 'Failed to add')
    else:
        form = AddForm()
    return render(request,'index.html',{'form':form})


 
    

