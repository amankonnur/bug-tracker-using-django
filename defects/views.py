from django.shortcuts import render,redirect
from defects.models import Defect,defect_screen_short
from django.contrib.auth.decorators import login_required
from defects.forms import DefectEditForm, Adddefect,FilterDefectForm
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from defects.utils import send_email_view

# Create your views here.

@login_required(login_url='login')
def defect_list(request):
    defects = Defect.objects.all()
    defects_count = Defect.objects.all().count()
    # Paginator1 = Paginator(page,5)
    # page_number = request.GET.get('pg')
    # page = paginator.get_page(page_number)
    context = {
        'defects': defects,
        'defects_count': defects_count
    }
    return render(request, 'defects/alldefects.html', context)


@login_required(login_url='login')
def description(request,id=0):
    defects = Defect.objects.get(id=id)
    defect_details = defect_screen_short.objects.filter(defect_name=defects)
    context = {
        'defects': defects,'defect_details': defect_details,
        'defect1':defect_details
    }
    return render(request, 'defects/description.html', context)


def edit_defect(request,id=0):
    defect = Defect.objects.get(id=id)
    if request.method == 'POST':
        form = DefectEditForm(request.POST,instance=defect)
        if form.is_valid():    
            form.save()

            return redirect('defect_list')
    else:
        form = DefectEditForm(instance=defect)

    form = DefectEditForm(instance=defect)
    return render(request, 'defects/editdefects.html', {'form': form})



def adddefect(request):
    if request.method == 'POST':
        form = Adddefect(request.POST)
        if form.is_valid():
            form.save()
            # user = 
            send_email_view(user.email)
            return redirect('defect_list')
    else:
        form = Adddefect()
    return render(request, 'defects/adddefects.html',{'form': form})


def filter(request):
    defects = Defect.objects.all()
    if request.method == 'POST':
        form = FilterDefectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['assignedto']

            # user = User.objects.get(username=name)

            # devname = 


    else:
        form = FilterDefectForm()
    return render(request,'defects/filter.html',{"form":form,'name':name,'defects':defects})