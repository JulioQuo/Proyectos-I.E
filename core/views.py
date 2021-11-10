from django.shortcuts import render, redirect
from .models import Libro
from .forms import ExtraForms, LibroForm, CustomUserForm
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth import login , authenticate
# Create your views here.
def home(request):
    data = {
        'libros':Libro.objects.all()
    }
    return render(request, 'core/home.html', data)


def galeria(request):
    data = {
        'libros':Libro.objects.all()
    }
    return render(request, 'core/galeria.html',data)

def listado_libro(request):
    libro = Libro.objects.all()
    data = {
        'libro': libro
    }
    return render(request, 'core/listado_libros.html',data)

@permission_required('core.add_libro')
def nuevo_libro(request):
    data = {
        'form':LibroForm()
    }
    if request.method == 'POST':
        formulario = LibroForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado Correctamente"
            
    return render(request, 'core/nuevo_libro.html',data)

def modificar_libro(request, id):
    libro = Libro.objects.get(id=id)
    data = {
        'form': LibroForm(instance=libro)
    }
    if request.method == 'POST':
        formulario = LibroForm(data=request.POST, instance=libro, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado Correctamente"
        data['form'] = LibroForm(instance=Libro.objects.get(id=id))

    return render(request, 'core/modificar_libro.html', data)

def eliminar_libro(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()

    return redirect(to="listado_libros")

def registro_usuario(request):
    data = {
        'form':CustomUserForm(),
        'form1':ExtraForms()
    }

    if request.method == 'POST':
        formulario = CustomUserForm(request.POST), ExtraForms(request.POST)
        formulario1 = ExtraForms(data=request.POST,files=request.FILES)
        if formulario.is_valid() | formulario1.is_valid():
            formulario.save()
            #autneticar y redirigir 
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username= username, password=password)
            login(request,user)
            return redirect(to='home')

    return render(request, 'registration/registrar.html', data)
def inicio(request):

    return render(request, 'core/ini.html')

def carrito(request):

    return render(request, 'core/carrito.html')
