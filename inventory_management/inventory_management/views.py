from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Equipment, Reservation
from .forms import EquipmentFilterForm, ReservationForm
from django.utils import timezone

@login_required
def make_reservation(request, equipment_id):
    equipment = get_object_or_404(Equipment, pk=equipment_id)
    error = ''
    
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            start_date = timezone.now().date()
            end_date = form.cleaned_data['end_date']

            if (end_date < start_date):
                error = 'End date must be greater than or equal to start date.'
            elif(equipment.quantity < 1):
                error = 'Item is out of stock.'
            else:
                reservation = Reservation(
                    equipment=equipment,  
                    user=request.user,  
                    start_date=start_date,  
                    end_date=end_date
                )
                reservation.save()
                return redirect('reservations')
    else:
        form = ReservationForm()

    context = {
        'equipment': equipment,
        'form': form,
        'error': error
    }
    return render(request, 'make_reservation.html', context)

@login_required
def reservations(request):
    reservations_list = Reservation.objects.filter(user=request.user)
    debug_message = '' 

    context = {'reservations_list': reservations_list, 'debug_message': debug_message, 'now': timezone.now().date()}
    return render(request, 'reservations.html', context)

@login_required
def delete_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    reservation.delete()
    return redirect('reservations')

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

@login_required
def admin(request):
    if request.user.is_staff:
        reservations_list = Reservation.objects.all()
        all_equipment = Equipment.objects.all()
        equipment_count = Equipment.objects.count()
        reservation_count = Reservation.objects.count()
        overdue_count = Reservation.objects.filter(end_date__lt=timezone.now().date()).count()
        equipment_quantity = 0
        for equipment in all_equipment:
            equipment_quantity += equipment.quantity

        context = {'now': timezone.now().date(), 'reservations_list': reservations_list, 'equipment_count': equipment_count, 'overdue_count': overdue_count, 'reservation_count': reservation_count, 'equipment_quantity': equipment_quantity}
        return render(request, 'admin.html', context)
    else:
        return redirect('equipment')

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