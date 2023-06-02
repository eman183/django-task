from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Course
# Create your views here.

def course(request):
        data=Course.objects.all()
       
        return render(request,"courses/course_list.html",{"courses":data})




def update_course(request,id):
        data=Course.objects.get(id=id)
        if (request.method=="POST"):
            Course.objects.filter(id=id).update(name=request.POST['name'],active=request.POST['active'])
            return HttpResponseRedirect("/course")
        return render(request,"courses/update_course.html",{"course":data})


def delete_course(request,ID):
        Course.objects.filter(id=ID).delete()
        return HttpResponseRedirect("/course")



def add_course(request):
        if ( request.method == "POST"):
          
          Course.objects.create(name=request.POST['name'])
          
        return render(request,"courses/add_course.html")
 