from django.shortcuts import get_object_or_404,render,redirect

from delivery.forms import DeliveryPersonnelForm, MealDeliveryForm
from delivery.models import DeliveryPersonnel, MealDelivery

# Delivery Views

def delivery_personnel_list(request):
    d_personnel_list = DeliveryPersonnel.objects.all()
    return render(request,'delivery/personnel_list.html',{'form':d_personnel_list})

def delivery_personnel_create_(request):
    form = DeliveryPersonnelForm()
    if request.method=='POST':
        form = DeliveryPersonnelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('delivery_personnel_list')
    context = {
        'form':form
    }
    return render(request,'delivery/d_personnel_create.html',context)

def delivery_personnel_update_(request,id):
    d_personnel_get = DeliveryPersonnel.objects.get(id=id)
    form = DeliveryPersonnelForm(instance=d_personnel_get)
    if request.method=='POST':
        form = DeliveryPersonnelForm(request.POST,instance=d_personnel_get)
        if form.is_valid():
            form.save()
            return redirect('delivery_personnel_list')
    context = {
        'form':form
    }
    return render(request,'delivery/d_personnel_create.html',context)

def delivery_personnel_delete_(request,id):
    d_personnel_get = DeliveryPersonnel.objects.get(id=id)
    d_personnel_get.delete()
    return redirect('delivery_personnel_list')


def meal_list(request):
    meals_list = MealDelivery.objects.all()
   
    return render(request,'delivery/meals_list.html',{'form':meals_list})

def meal_preparation_create_(request):
    form = MealDeliveryForm()
    if request.method=='POST':
        form = MealDeliveryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('meal_list')
    context = {
        'form':form
    }
    return render(request,'delivery/meal_delivery_form.html',context)

def meal_preparation_update_(request,id):
    meal_preparation_get = MealDelivery.objects.get(id=id)
    form = MealDeliveryForm(instance=meal_preparation_get)
    if request.method=='POST':
        form = MealDeliveryForm(request.POST,instance=meal_preparation_get)
        if form.is_valid():
            form.save()
            return redirect('meals_list')
    context = {
        'form':form
    }
    return render(request,'delivery/meal_delivery_form.html',context)


def meal_preparation_delete_(request,id):
    meal_preparation_get = MealDelivery.objects.get(id=id)
    meal_preparation_get.delete()
    return redirect('meal_list')