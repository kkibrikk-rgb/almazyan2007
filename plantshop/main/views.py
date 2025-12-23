from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import Plant, CustomUser

def home(request):
    plants = Plant.objects.filter(in_stock=True)
    paginator = Paginator(plants, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'shop/home.html', {'page_obj': page_obj})

def plant_detail(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    return render(request, 'shop/plant_detail.html', {'plant': plant})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'shop/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'shop/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@user_passes_test(lambda u: u.is_staff)
def custom_admin(request):
    users = CustomUser.objects.all()
    plants = Plant.objects.all()
    return render(request, 'shop/custom_admin.html', {'users': users, 'plants': plants})
