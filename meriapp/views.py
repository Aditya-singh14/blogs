from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Blog 
from .models import Contact
from django.core.mail import send_mail

# Create your views here.
def index(request):
    blog=Blog.objects.all()
    return render(request,'index.html',{'blogs':blog})


def register(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        firstname=request.POST.get('fname')
        lastname=request.POST.get('lname')
        username=request.POST.get('uname')
        if User.objects.filter(email=email).exists():
            messages.warning(request,'email already exists')
            return redirect('register')
        else:
            user =User(email=email,password=password,first_name=firstname,last_name=lastname,username=username)
            user.set_password(password)
            user.save()
            subject='About Registration'
            # message='Hi {uname}, You have been registered successfully on knowledge gainer blogs '
            # email_from='adisingh5213@gmail.com'
            # rec_list=[email,]           
            # send_mail(subject,message,email_from,rec_list)
            messages.success(request, 'User registered Successfully.')
            return redirect('/')
    return render(request,'register.html')


def login_user(request):
    if request.method=='POST':
        username = request.POST['uname']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect ('/')
        else:
            messages.warning(request,'Invalid credentials')
            return redirect('login')
    return render (request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def blogpost(request):
    if request.method=='POST':
        title=request.POST.get('title')
        content=request.POST.get('content')
        img=request.FILES['image']
        blog = Blog(title=title, content=content, user_id=request.user,Img=img)
        blog.save()
        messages.success(request,'Post Submitted')
        return redirect('/')
    return render(request,'blog_post.html')

def blog_detail(request,id):
    blog=Blog.objects.get(id=id)
    return render (request,'blog_detail.html',{'blog':blog})

def delete_post(request,id):
    blog=Blog.objects.get(id=id)
    blog.delete()
    messages.success(request,'Post Deleted Succesfully')
    return redirect('/')

def edit_post(request,id):
    blog=Blog.objects.get(id=id)
    if request.method=='POST':
        title=request.POST.get('title')
        content=request.POST.get('content')
        blog.title=title
        blog.content=content
        blog.save()    
        messages.success(request,'You edited your Blog')
        return redirect('/')
    return render(request,'edit.html',{'blog':blog})

def contact_form(request):
    if request.method=='POST':
        contact=Contact()
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        contact.first_name=firstname
        contact.last_name=lastname
        contact.email=email
        contact.phone=phone
        contact.message=message
        contact.save()
        messages.success(request,'Thank you for writing us')
        return redirect('/')
    return render(request,'contact_form.html')
    
def change_password(request):
    if request.method=='POST':
        newpass=request.POST.get('newpassword')
        u=User.objects.get(username=request.user.username)
        u.set_password(newpass)
        u.save()
        messages.success(request,'Your Password has been changed')
        return redirect('/')
    return render(request,'change_password.html')