from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MensajeContactoForm

def index(request):
    return render(request, 'home/index.html')

def servicios(request):
    return render(request, 'home/servicios.html')

def quienessomos(request):
    return render(request, 'home/quienessomos.html')

def contactenos(request):
    if request.method == 'POST':
        form = MensajeContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Tu mensaje ha sido enviado exitosamente!')
            return redirect('contactenos')
    else:
        form = MensajeContactoForm()
    return render(request, 'home/contactenos.html', {'form': form})
