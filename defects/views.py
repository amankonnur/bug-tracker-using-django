from django.shortcuts import render,redirect
from defects.models import Defect,defect_screen_short
from django.contrib.auth.decorators import login_required
from defects.forms import DefectEditForm, Adddefect
from django.core.paginator import Paginator

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
            return redirect('defect_list')
    else:
        form = Adddefect()
    return render(request, 'defects/adddefects.html',{'form': form})


# def cards(request):
#     defects = Defect.objects.all()
#     # defects_count = Defect.objects.all().count()
#     defects_count = len(list(map(Defect.objects.all())))
#     pending = Defect.objects.filter(defect_status='not started yet').count()
#     in_progress = Defect.objects.filter(defect_status='still in progress').count()
#     completed = Defect.objects.filter(defect_status='completed').count()
#     context = {
#         'defects': defects,
#         'defects_count': defects_count,
#         'pending': pending,
#         'in_progress': in_progress,
#         'completed': completed
#     }
#     print(context)
#     return render(request, 'accounts/profile.html', context)