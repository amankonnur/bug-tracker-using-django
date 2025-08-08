from django.shortcuts import render,redirect
from userapp.forms import updateprofileform, userform,userprofileform,updateform
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from defects.models import Defect


# Create your views here.
def index(request):
    registered = False
    form = userform
    form1 = userprofileform
    if request.method == 'POST':
        form = userform(request.POST)
        form1 = userprofileform(request.POST,request.FILES)
        if form.is_valid() and form1.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile = form1.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
    else:
        form = userform()
        form1 = userprofileform()
    
    context ={
        'form':form,
        'form1':form1,
        'registered':registered
    }
    return render(request,'accounts/index.html',context)



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse("Your account is disabled")
        else:
            return HttpResponse("please check your chredentials")
        
    return render(request,'accounts/login.html',{}) 


@login_required(login_url='login')
def home(request):
    return render(request,'accounts/home.html',{})

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('index')




@login_required(login_url='login')
def profile(request):
    defects = Defect.objects.all()
    defects_count = Defect.objects.all().count()
    # defects_count = len(list(map(Defect.objects.all())))
    pending = Defect.objects.filter(defect_status='not started yet').count()
    in_progress = Defect.objects.filter(defect_status='still in progress').count()
    completed = Defect.objects.filter(defect_status='completed').count()
    context = {
        'defects': defects,
        'defects_count': defects_count,
        'pending': pending,
        'in_progress': in_progress,
        'completed': completed
    }
    return render(request, 'accounts/profile.html', context)




@login_required(login_url='login')
def update(request):
    if request.method == 'POST':
        form = updateform(request.POST,instance=request.user)
        form1 = updateprofileform(request.POST,request.FILES,instance=request.user.userdata)
        if form.is_valid() and form1.is_valid():
            user = form.save(commit=False)
            user.save()

            profile = form1.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('profile')
    else:
        form = updateform(instance=request.user)
        form1 = updateprofileform(instance=request.user.userdata)
    return render(request,'accounts/update.html',{'form':form,'form1':form1})


