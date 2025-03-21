from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Command
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            if user.is_superuser:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponseForbidden("Accès refusé : vous n'êtes pas superutilisateur.")
        else:
            return render(request, 'commands/login.html', {'error': "Identifiants invalides"})
    return render(request, 'login.html')


def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})


def add_category(request):
    if request.method == "POST":
        title = request.POST.get('title')
        if title:
            Category.objects.create(title=title)
            return redirect('home')
    return render(request, 'add_category.html')


def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == "POST":
        category.delete()
        return redirect('home')
    return render(request, 'delete_category.html', {'category': category})


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    commands = Command.objects.filter(category=category)
    return render(request, 'category_detail.html', {'category': category, 'commands': commands})


def add_command(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        Command.objects.create(category=category, title=title, content=content)
        return redirect('category_detail', category_id=category_id)
    return render(request, 'add_command.html', {'category': category})


def edit_command(request, command_id):
    cmd = Command.objects.get(id=command_id)
    if request.method == "POST":
        cmd.title = request.POST.get('title')
        cmd.content = request.POST.get('content')
        cmd.save()
        return redirect('category_detail', category_id=cmd.category.id)
    return render(request, 'edit_command.html', {'command': cmd})


def delete_command(request, command_id):
    cmd = Command.objects.get(id=command_id)
    category_id = cmd.category.id
    if request.method == "POST":
        cmd.delete()
        return redirect('category_detail', category_id=category_id)
    return render(request, 'delete_command.html', {'command': cmd})

def user_logout(request):
    logout(request)
    return redirect('login')
