from django.shortcuts import get_object_or_404,render,redirect
from django.http import JsonResponse
from hospital.models import Patient, DietChart
from hospital.forms import PatientForm, DietChartForm


# Hospital Views
def patient_list_(request):
    patients = Patient.objects.all()

    return render(request,'hospital/patient_list.html',{'patient':patients})

def patient_create_(request):
    add_patient = PatientForm()
    if request.method=='POST':
        add_patient = PatientForm(request.POST)
        if add_patient.is_valid():
            add_patient.save(commit=True)
            return redirect('patient_list_create')
    context = {
        'form':add_patient
    }
    return render(request,'hospital/patient_form.html',context)

def patient_detail(request, id):
    patient = Patient.objects.get(id=id)
    context = {
        'patient_detail':patient
    }
    return render(request,'hospital/patient_detail.html',context)

def patient_update(request,id):
    update_patient = Patient.objects.get(id=id)
    form = PatientForm(instance=update_patient)
    if request.method== 'POST':
        form = PatientForm(request.POST,instance=update_patient)
        form.save()
        return redirect('patient_list_create')
    context = {
        'form':form
    }
    return render(request,'hospital/patient_form.html',context)

def patient_delete(request,id):
    patient_delete = Patient.objects.get(id=id)
    patient_delete.delete()
    return redirect('patient_list_create')


#diet-charts

def dietchart_list_(request):
   dietchart = DietChart.objects.all()
   return render(request,'hospital/diet_chart_list.html',{'dietchart':dietchart})

def dietchart_create_(request):
    form = DietChartForm(request.POST)
    if form.is_valid():
        form.save(commit=True)
        return redirect('diet_chart_list_create')
    else:
        form = DietChartForm()
    context = {
        'form':form
    }
    return render(request,'hospital/patient_form.html',context)

def dietchart_detail(request, id):
    dietchart = DietChart.objects.get(id=id)
    context = {
        'dietchart':dietchart
    }
    return render(request,'hospital/diet_chart_detail.html',context)

def dietchart_update(request,id):
    dietchart_patient = DietChart.objects.get(id=id)
    form = DietChartForm(instance=dietchart_patient)
    if request.method== 'POST':
        form = DietChartForm(request.POST,instance=dietchart_patient)
        form.save()
        return redirect('diet_chart_list_create')
    context = {
        'form':form
    }
    return render(request,'hospital/patient_form.html',context)

def dietchart_delete(request,id):
    dietchart_delete = DietChart.objects.get(id=id)
    dietchart_delete.delete()
    return redirect('diet_chart_list_create')