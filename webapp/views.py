from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Producto, Categoria
from django.db.models import Q
import json
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password, check_password

User = get_user_model()

def index(request):
    products = Producto.objects.all().order_by('-id')
    return render(request, 'index.html', {'productos': products})

def buscar_producto(request):
    query = request.GET.get('q')
    productos = Producto.objects.all()

    if query:
        productos = productos.filter(
            Q(nombre__icontains=query)
        )

    return render(request, 'index.html', {'productos': productos, 'query': query})

def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'detalle_producto.html', {'producto': producto})

def carrito(request):
    carrito_cookie = request.COOKIES.get('cart')
    if not carrito_cookie:
        return render(request, 'carrito.html', {'productos': [], 'total': 0})
    
    try:
        carrito = json.loads(carrito_cookie)
    except json.JSONDecodeError:
        carrito = []
    
    productos = []
    total = 0
    for item in carrito:

        producto = Producto.objects.get(id=item["id"])

        productos.append({
            'producto': producto.nombre,
            'subtotal': producto.precio * item["quantity"],
            'cantidad': item["quantity"]
        })


    return render(request, 'carrito.html', {'productos': productos, 'total': total})

def checkout(request):
    return render(request, 'checkout.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        password = request.POST['password']
        User.objects.create(
            username=username,
            email=email,
            address=address,
            phone=phone,
            password=make_password(password),
            role='cliente'
        )
        return redirect('login')
    
    return render(request, 'register.html')

def loginView(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Credenciales incorrectas'})
    return render(request, 'login.html')

def logoutView(request):
    logout(request)
    return redirect('login')


# Admin Views

def adminView(request):
    return render(request, 'administration/index.html')