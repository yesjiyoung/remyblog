from django.shortcuts import render, redirect
from django.contrib.auth.models import User #User에 대한 클래스를 가져온다!
from django.contrib import auth #계정에대한권한에 관한 내용을 가져온다~
# Create your views here.

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('home')          
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else :
            return render(request, 'home.html', {'error' : 'user or password is incorrect'}) #login.html지우고 login->home으로바꾸기
    else:
        return render(request, 'home.html')   

def logout(request):
    #if request.method == 'POST':
    auth.logout(request)
    return redirect('home')
    #else : 
     #   return render(request, 'home.html')