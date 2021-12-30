from django.shortcuts import render, redirect
from .models import WebForm
from .form import FromWebForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q



# Create your views here.
def loginUser(request):
    if request.user.is_authenticated:
        redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try: 
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Tài khoản không hợp lệ')
        
        user = authenticate(request, username=username, password=password )

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'mật khẩu không đúng')

    context = {}
    return render(request, 'login.html', context)

def logOut(request):
    logout(request)
    return redirect('home')

@login_required(login_url='/login')
def webForm(request):
    form = FromWebForm()
    members = WebForm.objects.all()
    if request.method == 'POST':
        WebForm.objects.create(
            tenhang = request.POST.get('tenhang'),
            dvt = request.POST.get('dvt'),
            soluong = request.POST.get('soluong'),
            dongia = request.POST.get('dongia')            
        )
    context = {'form': form, 'members': members}
    return render(request, 'home.html', context)

@login_required(login_url='/login')
def deleteGoods(request, pk):
    good = WebForm.objects.get(id=pk)
    if request.method == 'POST':
        good.delete()
        return redirect('home')

    return render(request, 'delete.html', {'good': good})

@login_required(login_url='/login')
def updateGood(request, pk):
    good = WebForm.objects.get(id=pk)
    form = FromWebForm(instance=good)

    if request.method == 'POST':
        form = FromWebForm(request.POST, instance=good)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form, 'good': good}
    return render(request, 'update.html', context)

def searchGood(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    members = WebForm.objects.filter(Q(tenhang__icontains=q))
    context = {'members': members, 'q': q}
    return render(request, 'search.html', context)