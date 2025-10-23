from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Cliente  
from .forms import ClienteForm
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
def index(request):
    return render(request, 'cliente/index.html', {
        'cliente': Cliente.objects.all()
    })

def ver_clientes(request, id):
    cliente = Cliente.objects.get(pk=id)
    return render(request, 'cliente/ver_clientes.html', {'cliente': cliente})

def add(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            nuevo_cliente_nombre = form.cleaned_data['nombre']
            nuevo_cliente_apellido = form.cleaned_data['apellido']
            nuevo_cliente_correo = form.cleaned_data['correo']
            nuevo_cliente_telefono = form.cleaned_data['telefono']
            nuevo_cliente_direccion = form.cleaned_data['direccion']
            nuevo_cliente_fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
        
            nuevo_cliente = Cliente(
                nombre=nuevo_cliente_nombre,
                apellido=nuevo_cliente_apellido,
                correo=nuevo_cliente_correo,
                telefono=nuevo_cliente_telefono,
                direccion=nuevo_cliente_direccion,
                fecha_nacimiento=nuevo_cliente_fecha_nacimiento,

            )

            nuevo_cliente.save()
            return render(request, 'cliente/add.html', {
                'form': ClienteForm(),
                'success': True
            })

    else:
        # ✅ Aquí cargas el formulario cuando entras a la página
        form = ClienteForm()

    return render(request, 'cliente/add.html', {'form': form})
def edit(request, id):
    cliente = Cliente.objects.get(pk=id)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('ver_clientes', id=cliente.id) 
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'cliente/edit.html', {
        'form': form,
        'success': False
    })
def delete_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    
    if request.method == "POST":
        cliente.delete()
        return redirect('delete_success')  # Redirige a la página de éxito
    
    # Si es GET, mostramos la confirmación
    return render(request, 'cliente/delete_confirm.html', {'cliente': cliente})

def delete_success(request):
    return render(request, 'cliente/delete_success.html')