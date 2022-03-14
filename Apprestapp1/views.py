
from Apprestapp1.models import *
from django.http import HttpResponse
from django.shortcuts import render
from Apprestapp1.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def inicio(request):

    restaurants = Restaurant.objects.order_by('-pk')[:4]
    # avatar = Avatar.objects.filter(user = request.user.id)
    return  render(request, "Apprestapp1/inicio.html", {"restaurants": restaurants})

def error(request):

    return render(request, "Apprestapp1/404.html")   
class RestaurantList(ListView):
    model = Restaurant
    template_name = "Apprestapp1/restaurant_list.html"

class RestaurantDetail(DetailView):
    model = Restaurant
    template_name = "templates/restaurant_detail.html"


class RestaurantCreate(LoginRequiredMixin,CreateView):
    model = Restaurant
    success_url = "/listarestaurants/"
    fields = ['nombre', 'categoria', 'informacion', 'propietario', 'imagen']
    # template_name = "appclase/cursos.html"


class RestaurantUpdate(LoginRequiredMixin,UpdateView):
    model = Restaurant
    success_url = "/listarestaurants/"
    fields = ['nombre', 'categoria', 'informacion', 'propietario', 'imagen']
    template_name= "Apprestapp1/restaurant_form.html"


class RestaurantDelate(LoginRequiredMixin,DeleteView):
    model = Restaurant
    success_url = "/listarestaurants/"
    template_name= "Apprestapp1/restaurant_confirm_delete.html"

def buscar(request):
    
    if  request.GET["nombre"]:

        nombre = request.GET['nombre'] 
        restaurants = Restaurant.objects.filter(nombre__icontains=nombre)

        return render(request, "/templates/resultado_busqueda.html", {"nombre":nombre, "restaurants":restaurants})

    else: 
        respuesta = "No enviaste datos"
    #No olvidar from django.http import HttpResponse
    return HttpResponse(respuesta)

def login_request(request):
    
    if request.method == 'POST':
        form = AuthenticationForm (request, data= request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request,user)
                

                return render(request, "Apprestapp1/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            
            else:
                return render(request, "Apprestapp1/inicio.html", {"mensaje": "Error, datos incorrectos"})
        
        else:
                return render(request, "Apprestapp1/inicio.html", {"mensaje":"Error, formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "Apprestapp1/login.html", {'form':form})

def register(request):
    
    if request.method == 'POST':
        
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "Apprestapp1/inicio.html", {"mensaje": "Usuario Creado :)"})

    else:
        form = UserRegisterForm()

    return render(request,"Apprestapp1/registro.html", {"form":form})


@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method =='POST':
        
        miFormulario = UserEditForm(request.POST)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()
            
            return render(request, "Apprestapp1/inicio.html")
    
    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})
    
    return render(request, "Apprestapp1/editarperfil.html", {"miFormulario":miFormulario, "usuario":usuario})    

def contacto(request):
    data = {'form': ContactoForm()}
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data ["mensaje"] = "Mensaje enviado!!!"
        else:
            data ["form"] = formulario
    return render(request, 'Apprestapp1/contacto.html', data)