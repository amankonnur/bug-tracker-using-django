from django.shortcuts import render,redirect
from defects.models import Defect,defect_screen_short
from django.contrib.auth.decorators import login_required
from defects.forms import DefectEditForm

# Create your views here.

@login_required(login_url='login')
def defect_list(request):
    defects = Defect.objects.all()
    context = {
        'defects': defects
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


"""
from django.core.paginator import Paginator

Paginator = Paginator(varname,5)
page_number = request.GET.get('pg')
varname = paginator.ger_page(page_number)
"""