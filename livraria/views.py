from django.shortcuts import render, get_object_or_404, redirect
from .models import Autor, Categoria, Livro
from django.http import HttpResponse
from livraria.forms import LivroForm
from django.contrib.auth import authenticate, login, logout
import logging

def logout_usuario(request):
    logout(request)
    return render(request, 'livraria/login.html', {}),

def cadastrar_livro(request):
        if request.method == "POST":
            form = LivroForm(request.POST, request.FILES)
            if form.is_valid():
                livro = form.save(commit=False)
                form.save()
                return redirect('detalhar_livro', id=livro.id)
        else:
            form = LivroForm()
        return render(request, 'livraria/editar_livro.html', {'form': form})

def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'livraria/listar_livros.html', {'livros': livros})

def listar_categorias(request):
    categorias = Categoria.objects.all()
    categoria = categorias.first() if categorias else None
    return render(request, 'livraria/listar_categorias.html', {'categorias': categorias, 'categoria': categoria})

def listar_autores(request):
    autores = Autor.objects.all()
    autor = autores.first() if autores else None
    return render(request, 'livraria/listar_autores.html', {'autores': autores, 'autor': autor})

def detalhar_livro(request, id):
    livro = get_object_or_404(Livro, pk=id)
    return render(request, 'livraria/detalhar_livro.html', {'livro': livro})

def editar_livro(request, id):
    livro = get_object_or_404(Livro, pk=id)
    if request.method == "POST":
        form = LivroForm(request.POST, request.FILES, instance=livro)
        if form.is_valid():
            livro = form.save(commit=False)
            form.save()
            return redirect('detalhar_livro', id=livro.id)
    else:
        form = LivroForm(instance=livro)
        
    return render(request, 'livraria/editar_livro.html', {'form': form})

def buscar_livro(request):
    if request.method == 'POST':
        infor = request.POST.get('infor')
        if infor:
            livros = Livro.objects.filter(nome__icontains=infor)
            return render(request, 'livraria/listar_livros.html', {'livros': livros})
        else:
            mensagem = "Por favor, forneça um termo de pesquisa válido."
            return render(request, 'livraria/mensagem.html', {'mensagem': mensagem})
    
    mensagem = "Método de solicitação inválido."
    return render(request, 'livraria/mensagem.html', {'mensagem': mensagem})

def page_login(request):
    return render(request, 'livraria/login.html', {})

def autenticar_usuario(request):
    mensagem = None

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
           login(request, user)
        livros = Livro.objects.all()
        return render(request, 'livraria/listar_livros.html', {'livros':livros})
    else:
        return render(request, 'livraria/login.html',{})

def minha_view(request):
    livros = Livro.objects.all()
    for livro in livros:
        logger.info(f'Caminho da imagem: {livro.imagem.path}')

