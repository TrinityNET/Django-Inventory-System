from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Equipment
from .forms import EquipmentFilterForm

@login_required
def equipment(request):
    equipment_list = Equipment.objects.all()
    form = EquipmentFilterForm(request.POST)
    debug_message = ''
    
    if request.method == 'POST' and form.is_valid():
        location = form.cleaned_data.get('location')
        audit = form.cleaned_data.get('audit')
        equipment_type = form.cleaned_data.get('equipment_type')

        if location:
            equipment_list = equipment_list.filter(location=location)
        if audit:
            equipment_list = equipment_list.filter(audit=audit)
        if equipment_type:
            equipment_list = equipment_list.filter(type=equipment_type)  
    context = {'equipment_list': equipment_list, 'debug_message': debug_message, 'form': form}
    return render(request, 'equipment.html', context)

def user_logout(request):
    logout(request)
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('equipment')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
