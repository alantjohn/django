from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from students.models import CustomUser
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        cp=request.POST['cp']
        f=request.POST['f']
        l=request.POST['l']
        e=request.POST['e']
        pl=request.POST['pl']
        ph=request.POST['ph']

        if(p==cp):
            user=CustomUser.objects.create_user(username=u,password=p,first_name=f,last_name=l,email=e,place=pl,phone=ph)
            user.save()
            return redirect('books:home')
        else:
            return HttpResponse('Password not same')
    return render(request, 'register.html')

def user_login(request):
    if(request.method=="POST"):
        u = request.POST['u']
        p = request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('books:home')
        else:
            return HttpResponse('Invalid')
    return render(request,'login.html')
@login_required
def user_logout(request):
    logout(request)
    return redirect('books:home')

