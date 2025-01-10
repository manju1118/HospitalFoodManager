from django.shortcuts import get_object_or_404,render,redirect

from pantry.models import PantryStaff,MealPreparation
from pantry.forms import PantryStaffForm, MealPreparationForm


# Pantry Views
def pantry_staff_list(request):
    pantry_staff = PantryStaff.objects.all()
    context = {
        "form":pantry_staff
    }
    return render(request,'pantry/staff_list.html',context)

def pantry_staff_create_(request):
    form = PantryStaffForm()
    if request.method=='POST':
        form = PantryStaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pantry_staff_list')
    context = {
        'form':form
    }

    return render(request,'pantry/pantry_staff_create.html',context)

def get_pantry_detail(request,id):
    get_staff = PantryStaff.objects.get(id=id)
    context = {
        'form':get_staff
    }
    return render(request,'pantry/get_pantry_detail.html',context)



def staff_update(request,id):
    staff_update_ = PantryStaff.objects.get(id=id)
    form = PantryStaffForm(instance=staff_update_)
    if request.method== 'POST':
        form = PantryStaffForm(request.POST,instance=staff_update_)
        form.save()
        return redirect('pantry_staff_list')
    context = {
        'form':form
    }
    return render(request,'pantry/pantry_staff_create.html',context)


def staff_delete(request,id):
    pantry_staff_delete = PantryStaff.objects.get(id=id)
    pantry_staff_delete.delete()
    return redirect('pantry_staff_list')
