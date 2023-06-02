from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from . models import Trainee
# from trainee.models import *
# Create your views here.
def index(request):
        return render(request,"base.html")
    
def login(req):
    context={}
    if(req.method=='POST'):
        u=Trainee.objects.filter(email=req.POST['email'],password=req.POST['password'])
        if(len(u)!=0):
            #add username in session
            req.session['name']=u[0].name
            return HttpResponseRedirect('/course')
        else:
            context['msg']='invalid email or password'
    return render(req,'trainee/login.html',context=context)


def register(request):
        if ( request.method == "POST"):
          
          Trainee.objects.create(name=request.POST['name'],email=request.POST['email'],password=request.POST['password'])
        #     name=request.POST.get('name')
        #     print(name)
        #     email=request.POST.get('email')
        #     print(email)

        #     password=request.POST.get('password')
        #     print(password)
        #     data=Trainee(email=email,password=password)
            # if ( request.method == "POST"):
            #   data.save()
        return render(request,"trainee/register.html")

    
trainee=[
     {"id":"1","name":"ali"},
     {"id":"2","name":"ahmed"},
     {"id":"3","name":"mai"},


]
def list_trainee(request):
     
        data=Trainee.objects.all()
        return render(request,"trainee/list_trainee.html",{"trainee":data})


def update_trainee(request,ID):
        data=Trainee.objects.get(id=ID)
        if (request.method=="POST"):
            Trainee.objects.filter(id=ID).update(name=request.POST['name'],email=request.POST['email'],password=request.POST['password'])
            return HttpResponseRedirect("/alltrainee")
        return render(request,"trainee/update_trainee.html",{"trainee":data})



def delete_trainee(request,id):
        Trainee.objects.filter(id=id).delete()
        return HttpResponseRedirect("/alltrainee")


def logout(request):
    request.session.clear()
    return HttpResponse('Logout')
