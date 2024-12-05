from django.shortcuts import render, get_object_or_404, redirect
from ..models import Usuario
from .forms import UserForm
from django.contrib.auth.hashers import make_password

def user_list(request):
    users = Usuario.objects.filter(role='administrativo')
    return render(request, 'users/index.html', {'users': users})

def user_create(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        role = 'administrativo'

        Usuario.objects.create_user(
            username=username,
            email=email,
            address=address,
            phone=phone,
            password=password,
            role=role,
        )
        return redirect('users:list')
    
    else:
        form = UserForm()

    return render(request, 'users/create.html', {'form': form})

def user_edit(request, pk):
    user = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        if username and email:
            user.username = username
            user.email = email
            user.phone = phone
            user.address = address

            if password:
                user.password = make_password(password)

            user.save()
            return redirect('users:list')
    else:
        form = UserForm(instance=user)

    return render(request, 'users/edit.html', {'form': form})

def user_delete(request, pk):
    user = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('users:list')
    
    return render(request, 'users/delete.html', {'user': user})
