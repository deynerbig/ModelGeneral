from django.shortcuts import render,redirect
from ModelApp2.form import formTienda
from ModelApp2.models import tienda
# Create your views here.

def index (request):
    return render (request,'index.html')

def tiendas(request):
    #obtenemos los objetos de tienda 
    tiendita=tienda.objects.all()
    #en un diccionario capturamos los datos que tenga el objeto tiendita 
    data={'Tienda':tiendita}
    # y por ultimo devolvemos a donde debe verse la informacion
    return render(request,'Tienda.html',data)

def AgregarProductos(request):
    #lo primero es que llamamos a lo que recuperaba todos lo datos de xammp
    form=formTienda()
    if request.method=='POST':
        form=formTienda(request.POST)
        if form.is_valid():
            form.save()
        return index (request)
    data1={'form':form}
    return render(request,'AgregarProducto.html',data1)

def eliminarinfo(request,id):
    market=tienda.objects.get(id=id)
    market.delete()
    return render(request,'Tienda.html')

def actualizarinfo(request,id):
    market=tienda.objects.get(id=id)#esto es de eliminar
    form=formTienda(instance=market)#es la unica linea que hay que crear
    if request.method=='POST':#de aqui para abajo es copia de registrar producto
        form=formTienda(request.POST,instance=market)
        if form.is_valid():
            form.save()
        return index (request)
    data1={'form':form}
    return render(request,'AgregarProducto.html',data1)


