from django.shortcuts import render,redirect
from register.models import student_master
from .models import admin_master
from django.contrib.auth import logout
# Create your views here.
def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Try to authenticate as an admin
        try:
            obj = admin_master.objects.get(email=email, password=password)
            request.session['email'] = obj.email
            return redirect('ahome')
        except admin_master.DoesNotExist:
            pass

        # If not admin, try to authenticate as a student
        try:
            obj = student_master.objects.get(email=email, password=password)
            request.session['email'] = obj.email
            return redirect('shome')
        except student_master.DoesNotExist:
            # Handle invalid credentials here
            # For example, you might want to set an error message
            context = {'error': 'Invalid email or password'}
            return render(request, "login.html", context)

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect('dashboard')
