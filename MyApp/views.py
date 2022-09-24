from django.shortcuts import render,redirect
from .models import Add_To_Cart
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.contrib import messages
def register(request):
    form=UserForm()
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registered Successfully! Login to continue")
            return render(request,"login.html")
    context={'form':form}
    return render(request,"register.html",context)
from MyApp.forms import UserForm
def createaccount(request):
    return render(request, 'CreateAccount.html')
# Create your views here.
