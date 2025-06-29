from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse, request
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.core.files.storage import FileSystemStorage
import re

from django.contrib.auth import authenticate,login,logout

from django.contrib import messages

# Create your views here.
def homedesign(request):
    return render(request ,'homedesign.html') 

def page(request):
    return render(request ,'page.html') 

def detect(request):
	if request.method == 'POST':
	    uploaded_file = request.FILES['document']
	    fs = FileSystemStorage()
	    name = fs.save(uploaded_file.name,uploaded_file)
	    url = fs.url(name)
	    print(url)
	    context = {'url' : url }
	else:
		context = {'url' : " "}

	return render(request,'disease_detect.html',context)

def dis_detect(request):
	if request.method == 'POST':
	  name1  = request.POST.get('uploaded_image')
	  print (name1)
	context = {'xyz' : name1}
	return redirect(request,'disease_detect.html',context)
     
def logoutUser(request):
	logout(request)
	return redirect('homedesign')

def loginPage(request):
	
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('page')
			else:
				messages.info(request, 'Username or Password is incorrect')

		context = {}
		return render(request, 'login.html', context)
    

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
           form = CreateUserForm(request.POST)
           if form.is_valid():
               form.save()
               user = form.cleaned_data.get('username')
               messages.success(request, 'Your Account has been created succesfully.' )
               return redirect('login')


    context = {'form':form}
    return render(request,'register.html',context )