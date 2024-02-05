from django.shortcuts import render
from books.models import Book
from books.forms import Bookform
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'home.html')

@login_required
def addbooks(request):
    if(request.method=="POST"):
        a=request.POST['a']
        b=request.POST['b']
        c=request.POST['c']
        d=request.FILES['d']
        e=request.FILES['e']
        f=Book.objects.create(title=a, author=b, price=c,pdf=d,cover=e)
        f.save()
        return viewbooks(request)
    return render(request,'addbooks.html')
@login_required
def addbooks1(request):
    if(request.method=="POST"):
        form=Bookform(request.POST)
        if form.is_valid():
            form.save()
        return viewbooks(request)
    form=Bookform()
    return render(request,'addbooks1.html', {'forms':form})

@login_required
def factorial(request):
    if(request.method=="POST"):
        num=int(request.POST['n'])
        f=1
        for i in range(1,num+1):
            f=f*i
        return render(request, 'factorial.html', {'factorial':f})

    return render(request, 'factorial.html')

def bookdetail(request,p):
    b=Book.objects.get(id=p)
    return render(request, 'book.html', {'b':b} )

def bookdelete(request,p):
    b = Book.objects.get(id=p)
    b.delete()
    return viewbooks(request)

def bookedit(request,p):
    b = Book.objects.get(id=p)
    if (request.method == "POST"):
        form = Bookform(request.POST,request.FILES,instance=b)
        if form.is_valid():
            form.save()
        return viewbooks(request)
    form=Bookform(instance=b)
    return render(request, 'edit.html',{'form':form})

def search(request):
    query=""
    b=None
    if(request.method=="POST"):
        query=request.POST['q']
        if(query):
            b= Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
    return render(request, 'search.html',{'query':query , 'b':b})

@login_required
def viewbooks(request):
    k=Book.objects.all()

    return render(request, 'viewbooks.html',{'b':k})

