from django.shortcuts import render,HttpResponseRedirect,redirect
from app1.forms import SoftwareForm
from app1.models import SoftwareRoles


def Software(request):
    software_form = SoftwareRoles.objects.all()
    form = SoftwareForm()
    if request.method=='POST':
        form = SoftwareForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        else:
            print("invalid form")
    return render(request,'newtask.html',{'software_form':software_form,'form':form})


def delete_data(request,pk):
        pi = SoftwareRoles.objects.filter(pk=pk)
        pi.delete()
        return HttpResponseRedirect('/')


def update(request,pk):
    pi = SoftwareRoles.objects.get(pk=pk)
    form = SoftwareForm(request.POST,instance=pi)
    if form.is_valid():
        form.save()
        pi=SoftwareRoles.objects.all()
        return redirect('/') 
    return render(request, 'newtask2.html',{'pi':pi,'form':form})
