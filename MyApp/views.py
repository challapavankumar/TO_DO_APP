from django.shortcuts import render,redirect
from .forms import TODOFORM
from .models import Todo

from django.contrib import messages
# Create your views here.
def home(request):
    if request.method=='POST':
        form=TODOFORM(request.POST or None)
        if form.is_valid():
            form.save()
            all_items=Todo.objects.all()
            messages.success(request,('Item has been added to the list'))
            return render(request,'temp/home.html',{'all_items':all_items})
    else:
        all_items=Todo.objects.all()
        return render(request,'temp/home.html',{'all_items':all_items})
def about(request):
    first_name="chowdary"
    last_name="challa"

    context={'first_name':first_name,'last_name':last_name }
    return render(request,'temp/about.html',context)
def delete(request,list_id):
    item=Todo.objects.get(pk=list_id)
    item.delete()
    messages.success(request,('Item has been deleted from the list'))
    return redirect('home')
def cross(request,list_id):
    item=Todo.objects.get(pk=list_id)
    item.completed=True
    item.save()
    return redirect('home')
def uncross(request,list_id):
    item=Todo.objects.get(pk=list_id)
    item.completed=False
    item.save()
    return redirect('home')
def edit(request,list_id):
    if request.method=='POST':
        item=Todo.objects.get(pk=list_id)
        form=TODOFORM(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
        messages.success(request,('Item has been edited '))
        return redirect('home')

    else:
        item=Todo.objects.get(pk=list_id)
        all_items=Todo.objects.all()
        return render(request,'temp/home.html',{'item':item,'all_items':all_items})