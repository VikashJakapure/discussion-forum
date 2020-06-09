from django.shortcuts import render,HttpResponseRedirect
from firstapp.models import Employee
from firstapp.forms import NewEmployeeForm
# Create your views here.  django forms by save method it is not inline factory project name is changed.
def display(request):
    E=Employee.objects.all()
    return render(request,'firstapp/display.html',{'E':E})

def add(request):
    E=NewEmployeeForm()
    if request.method=='POST':
        form=NewEmployeeForm(request.POST)
        eno=request.POST.get('eno')
        ename = request.POST.get('ename')
        esal = request.POST.get('esal')
        eaddr = request.POST.get('eaddr')
        email = request.POST.get('email')
        obj=Employee(eno=eno,ename=ename,esal=esal,eaddr=eaddr,email=email)
        obj.save()
        return HttpResponseRedirect ('/display/')
    return render(request,'firstapp/form.html',{'E':E})

def update(request,id):
    data=Employee.objects.get(pk=id)
    initial={'eno':data.eno,'ename':data.ename,'esal':data.esal,'eaddr':data.eaddr,'email':data.email}

    form=NewEmployeeForm(initial=initial)
    if request.method=='POST':
        form=NewEmployeeForm(request.POST)
        if form.is_valid():
            data.eno = request.POST.get('eno')
            data.ename = request.POST.get('ename')
            data.esal = request.POST.get('esal')
            data.eaddr = request.POST.get('eaddr')
            data.email = request.POST.get('email')
            #obj = Employee(eno=eno, ename=ename, esal=esal, eaddr=eaddr, email=email) used in create
            data.save()

        return HttpResponseRedirect ('/display/')
    return render(request,'firstapp/update.html',{'form':form,'data':data})

# def add(request):
#     E=NewEmployeeForm()
#     if request.method=='POST':
#         form=NewEmployeeForm(request.POST)
#         eno=request.POST.get('eno')
#         ename = request.POST.get('ename')
#         esal = request.POST.get('esal')
#         eaddr = request.POST.get('eaddr')
#         email = request.POST.get('email')
#      #create form    # Employee save form.objects.create(
#         #     eno=eno,
#         #     ename=ename,
#         #     esal=esal,
#         #     eaddr=eaddr,
#         #     email=email,
#         # )
#         obj=Employee(eno=eno,ename=ename,esal=esal,eaddr=eaddr,email=email)
#         obj.save()
#         return HttpResponseRedirect ('/display/')
#     return render(request,'firstapp/form.html',{'E':E})
#
# def update(request,id):
#     data=Employee.objects.get(pk=id)
#     initial={'eno':data.eno,'ename':data.ename,'esal':data.esal,'eaddr':data.eaddr,'email':data.email}
#     form=NewEmployeeForm(initial=initial)
#     if request.method=='POST':
#         form=NewEmployeeForm(request.POST)
#         # if form.is_valid():
#         #     form.save()
#         eno = request.POST.get('eno')
#         ename = request.POST.get('ename')
#         esal = request.POST.get('esal')
#         eaddr = request.POST.get('eaddr')
#         email = request.POST.get('email')
#         obj = Employee(eno=eno, ename=ename, esal=esal, eaddr=eaddr, email=email)
#         obj.save()
#
#         return HttpResponseRedirect ('/display/')
#     return render(request,'firstapp/update.html',{'form':form,'data':data})
