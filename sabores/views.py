from django.shortcuts import render, redirect
from .models import Sabor
from .forms import SaborForm

def agregar_sabor(request):
    if request.method == 'POST':
        form = SaborForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_sabores')
    else:
        form = SaborForm()

    return render(request, 'sabores/agregar_sabor.html', {'form': form})

def listar_sabores(request):
    sabores = Sabor.objects.all()
    return render(request, 'sabores/listar_sabores.html', {'sabores': sabores})

def buscar_sabores(request):
    query = request.GET.get('q', '')
    sabores = Sabor.objects.filter(nombre__icontains=query)
    return render(request, 'sabores/listar_sabores.html', {'sabores': sabores, 'query': query})
