from django.shortcuts import render
from .models import student_master

# Create your views here.
def register(request):
    if request.method=="POST" :
        name=request.POST["name"]
        branch=request.POST["branch"]
        year=request.POST["year"]
        sec=request.POST["sec"]
        mob=request.POST["mob"]
        email=request.POST["email"]
        password=request.POST["password"]
        ob=student_master.objects.create(name=name,branch=branch,year=year,sec=sec,email=email,mob=mob,password=password,)
        ob.save()
        return render(request,"register.html",{'msg':"registation sucessful..."})
    return render(request,"register.html")
