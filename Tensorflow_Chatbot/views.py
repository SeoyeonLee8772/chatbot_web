from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
#from django.contrib.auth.models import User
from chatapp.models import User, UserInformation, University
from django.contrib import auth
from django.contrib.auth import login, authenticate, logout


def chat(request):
    template = loader.get_template('chat.html')
    return HttpResponse(template.render({}, request))

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render({}, request))

def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            username = request.POST['username']
            User.objects.create(
                user_id=request.POST["username"], password=request.POST["password1"])
            UserInformation.objects.create(
                user_id=request.POST["username"], name=request.POST["name"],
                birth=request.POST["birth"], sex=request.POST["sex"],
                email=request.POST["email"], phone=request.POST["phone"],
                univname=request.POST["univname"])
            University.objects.create(
                univname=request.POST["univname"], major=request.POST["major"],
                grade=request.POST["grade"])
            member = UserInformation.objects.get(user_id=username)
            request.session['user']= member.name
            return redirect('home')
        return render(request, 'signup.html')
    return render(request, 'signup.html')

def Userlogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            member1 = User.objects.get(user_id=username)
            member2 = UserInformation.objects.get(user_id=username)
            if password == member1.password:
                request.session['user']= member2.name
                return redirect('home')
            else:
                return render(request, 'login.html', {'error':'비밀번호를 다시 확인해주세요.'})
        except:
            return render(request, 'login.html', {'error':'아이디가 존재하지 않습니다.'})
    return render(request, 'login.html')

# 로그아웃
def Userlogout(request):
    # logout으로 POST 요청이 들어왔을 때, 로그아웃 절차를 밟는다.
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    # logout으로 GET 요청이 들어왔을 때, 로그인 화면을 띄워준다.
    return render(request, 'login.html')