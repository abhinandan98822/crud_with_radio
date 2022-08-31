from re import A
from django.shortcuts import render,redirect
from . models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def Register(request):
    if request.method=='POST':
        Name=request.POST['name']
        Last_name=request.POST['lastname']
        Username=request.POST['username']
        Email=request.POST['email']
        Password=request.POST['psw']
        Confirm_Password=request.POST['cpsw']
        Salary=request.POST['salary']
        Gender=request.POST['gender']
        data=Student(name=Name,lastname=Last_name,username=Username,email=Email,password=Password,salary=Salary,gender=Gender)
        data.save()
    return render(request,'register.html')    

def Table(request):
    data=Student.objects.all()
    # mydata = Student.objects.values_list('username')
    a=data.values('gender')
    print(a)

    context={'data':data,'a':a}

    return render(request,'table.html',context)

def Delete(request,id):
    data=Student.objects.get(id=id)
    data.delete()
    return redirect('table')    

def Edit(request,id):
    print('__working')
    data=Student.objects.get(id=id)

    print(data.gender)
    return render (request,'edit.html',{'data':data})
