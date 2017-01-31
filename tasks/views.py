from django.shortcuts import render, redirect, get_object_or_404
from .models import Errand, Category
from .forms import LoginForm, ErrandForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def sign_in(request):
    form = LoginForm()
    if request.method == "GET":
        logout(request)
        return render(request, 'tasks/login.html', {'form': form})

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if not user:
        error = "Login failed"
        return render(request, 'tasks/login.html', {'form': form, 'error': error})
    else:
        login(request, user)
        return redirect('index')

@login_required(login_url='/tasks/')
def index(request):
    user = request.user
    errands = Errand.objects.filter(user=user)
    categories = Category.objects.all()
    return render(request, 'tasks/index.html', {'errands': errands,
                                                'categories': categories})

@login_required(login_url='/tasks/')
def new_task(request):
    if request.method == "GET":
        form = ErrandForm()
        return render(request, 'tasks/save_task.html', {'form': form})

    form = ErrandForm(request.POST)
    if form.is_valid():
        errand = form.save(commit=False)
        errand.user = request.user
        errand.save()
        return redirect('index')
    else:
        return render(request, 'tasks/save_task.html', {'form': form})

@login_required(login_url='/tasks/')
def edit_task(request, pk):
    errand = get_object_or_404(Errand, pk=pk)
    if request.method == "GET":
        form = ErrandForm(instance=errand)
        return render(request, 'tasks/save_task.html', {'form': form})

    form = ErrandForm(request.POST, instance=errand)
    if form.is_valid():
        errand = form.save(commit=False)
        errand.user = request.user
        errand.save()
        return redirect('index')
    else:
        error = "Something went wrong!"
        return render(request, 'tasks/save_task.html', {'form': form, 'error': error})

@login_required(login_url='/tasks/')
def delete_task(request, pk):
    errand = get_object_or_404(Errand, pk=pk)
    if request.method == "DELETE":
        print "Here"
        errand.delete()
        return redirect('index')


@login_required(login_url='/tasks/')
def sign_out(request):
    logout(request)
    return redirect('sign_in')
