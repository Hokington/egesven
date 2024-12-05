from webapp.models import Producto, Categoria, Pedido, DetallePedido, Pago, Despacho
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now
from django.http import JsonResponse
from django.db.models import Q
import json

User = get_user_model()

def index(request):
    products = Producto.objects.filter(stock__gt=0).order_by('-id')
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
    carrito = request.COOKIES.get('cart')
    carrito = json.loads(carrito)

    total = 0
    for item in carrito:
        producto = Producto.objects.get(id=item["id"])
        subtotal = producto.precio * item["quantity"]
        total += subtotal
    
    if request.method == 'POST':
        usuario = request.user

        pedido = Pedido.objects.create(
            usuario=usuario,
            estado='Pagado'
        )

        for item in carrito:
            producto = get_object_or_404(Producto, id=item["id"])
            DetallePedido.objects.create(
                pedido=pedido,
                producto=producto,
                cantidad=item["quantity"]
            )
            producto.stock -= item["quantity"]
            producto.save()

        Pago.objects.create(
            metodo='Tarjeta',
            monto=total,
            estado='Procesado',
            pedido=pedido,
            usuario=usuario
        )

        # Crear el despacho
        Despacho.objects.create(
            direccion_envio=request.POST.get('direccion_envio'),
            fecha_envio=now().date(),
            estado_despacho='Preparando',
            pedido=pedido
        )

        # Limpiar el carrito de la sesión
        return redirect('success')

    return render(request, 'checkout.html', {'total': total})

def success(request):
    return render(request, 'success.html')

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

def deliveries(request):
    pedidos = Pedido.objects.all()
    pagos = Pago.objects.all()
    despachos = Despacho.objects.all()

    return render(request, 'administration/deliveries.html', {
        'pedidos': pedidos,
        'pagos': pagos,
        'despachos': despachos,
    })