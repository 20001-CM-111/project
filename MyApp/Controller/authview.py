from django.shortcuts import render,redirect
from django.contrib import messages
from MyApp.forms import UserForm
def register(request):
    form=UserForm()
    context={'form':form}
    return render(request,"register.html",context)
