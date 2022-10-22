from django.contrib import messages
from django.shortcuts import render, redirect
from quiz.forms import addQuestionform
from rest_framework import generics
from rest_framework.response import Response
from .models import Quizze
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import time 

def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('home')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('home')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('home')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!!")
        
        return redirect('signin')

    return render(request, "signup.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            signin(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, " index.html",{"fname":fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('ProfileDetail')
    
    return render(request, "signin.html")

def result(request):
    return render(request,'result.html')

def addquestion(request):
    return render(request,'addquestion.html')

def signout(request):
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')

def quizee(request):
    if request.method == 'POST':
        return render(request,'result.html',context)
    else:
        questions=Quizze.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'home.html',context)   

class ProfileDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        queryset = Quizze.objects.all()
        return Response({'queryset': queryset})

def addQuestion(request):    
    if request.user.is_staff:
        form=addQuestionform()
        if(request.method=='POST'):
            form=addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'addQuestion.html',context)
    else: 
        return redirect('home') 

    
