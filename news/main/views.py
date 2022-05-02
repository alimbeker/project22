from dataclasses import field
from hashlib import new
from multiprocessing import context
from sre_constants import SUCCESS
from urllib import response
from django.http import HttpResponse
from django.shortcuts import redirect, render
from . models import *
from .forms import *
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import admin_only, unauthenticated_user, allowed_users
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

@unauthenticated_user
def loginPage(request):
	if request.user.is_authenticated:
		return redirect('project')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('project')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'main/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

@unauthenticated_user
def registerPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')


			messages.success(request, 'Account was created for ' + user)

			return redirect('login')
			

	context = {'form':form}
	return render(request, 'main/register.html', context)





@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def index(request):
    
    if request.method == "POST":
        form = MvideoForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video-upload')
    else:
        form = MvideoForm()
        
    var = {'form': form}
    return render(request, 'main/index.html', var)


@login_required(login_url='login')
@admin_only
def newproject(request):
    var = MenPrize.objects.all()
    return render(request, 'main/newproject.html', {'var': var})




@login_required(login_url='login')
def men(request):
    inf = Men.objects.all()
    return render(request, 'main/men.html', {'inf2': inf})

@login_required(login_url='login')
def women(request):
    infw = Women.objects.all()
    return render(request, 'main/women.html', {'infw': infw})


@allowed_users(allowed_roles=['customer'])
def form(request):
    post = Articles.objects.all()
    return render(request, 'main/form.html', {'post': post})

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def news_home(request):
    error = ' '
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sportnews')
        else:
            error = 'Form was uncorrect'

    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/news_home.html', data)


def create(request):
    return render(request, 'main/create.html')



class NewsDetailView(DetailView):
    model = Articles
    template_name = 'main/details_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'main/news_home.html'

    form_class = ArticlesForm


def delete(request, id):
    al = Articles.objects.get(id=id)
    al.delete()
    return redirect("sportnews")


def forupload(request):
    video = Mvideo.objects.all()

    return render(request, 'main/forupload.html', {'video' : video})

def userPage(request):
    context={}
    return render(request, 'main/user.html', context)

def managerPage(request):
    return render(request, 'main/manager.html')    

def test(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'worldhello521@gmail.com', ['200103054@stu.sdu.edu.kz'], fail_silently=True)
            if mail:
                messages.success(request, 'Email is send!')
                return redirect('test')
            else:
                messages.error(request,'Sending error!')
        else:
            messages.error(request, 'Register error!')
    else:
        form=ContactForm()
    return render(request, 'main/test.html', {'form':form})                        

