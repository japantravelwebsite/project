from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages
from .models import User
from .models import picture_db, Book
import time
from django.db import connection
from django.shortcuts import render
from django.db.models import Q

import logging
logger = logging.getLogger('my')
logger2 = logging.getLogger('my2')
# Create your views here.
login_user_name = 'None'

def login_view(request):
    global login_user_name
    logger.info("LOAD LOGIN PAGE")
    msg = "_"
    if request.method == "POST":
#        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        
        login_user_name = username
        user = authenticate(username = username, password = password)
        if user is not None:
            print("인증성공")
            msg = "로그인성공"
            logger.info("USER:%s LOGIN SUCCESSED", login_user_name)
            login(request, user)
        else:
            print("인증실패")
            logger.info("USER:%s LOGIN FAILED", login_user_name)
            messages.info(request, "입력이 잘못되었습니다.")
            msg = "입력실패"
            
    return render(request, "users/login2.html",{'msg':msg})#20230312김정현

def logout_view(request):
    logger.info("LOAD LOGOUT PAGE")
    logout(request)
    logger.info("USER:%s LOGOUT SUCCESSED", login_user_name)
    return redirect("user:login")

def signup_view(request):
    global login_user_name
    logger.info("LOAD SIGNUP PAGE")
    msg = "_"
    if request.method == "POST":
        username =request.POST["username"]
        password =request.POST["password"]
        firstname =request.POST["firstname"]
        lastname =request.POST["lastname"]
        email =request.POST["email"]
        student_id =request.POST["student_id"]
        login_user_name = username
        if len(username)*len(password)*len(firstname)*len(lastname)*len(email)*len(student_id) != 0: 
            print(request.POST)
            user = User.objects.create_user(username, email, password)
            user.last_name = lastname
            user.first_name = firstname
            user.student_id = student_id
            user.save()
            logger.info("USER:%s SIGNUP SUCCESSED", login_user_name)
            return redirect("user:login")
        else:
            print("빈칸오류")
            msg = "빈칸을 모두 채워주세요"
            logger.info("USER:%s SIGNUP FAILED", login_user_name)
            # messages.info(request, "빈칸을 모두 채워주세요")
    return render(request, "users/signup.html",{'msg':msg})

def GetNagoya(request):
    logger.info("USER:%s LOAD NAGOYA PAGE", login_user_name)
    imgs1 = Book.objects.filter(Q(location="nagoya") & Q(people="A"))
    imgs2 = Book.objects.filter(Q(location="nagoya") & Q(people="N"))
    imgs3 = Book.objects.filter(Q(location="nagoya") & Q(people="C"))
    imgs4 = Book.objects.filter(Q(location="nagoya") & Q(people="J"))
    #imgs = picture_db.objects.get(location = "Toyama")
    return render(request, "users/Nagoya.html", {"imgs1" : imgs1, "imgs2" : imgs2, "imgs3" : imgs3, "imgs4" : imgs4 })


def GetTakayama(request):
    logger.info("USER:%s LOAD TAKAYAMA PAGE", login_user_name)
    # print(logger.info("%s TAKAYAMA INFO", login_user_name) +"test")
    imgs1 = Book.objects.filter(Q(location="takayama") & Q(people="A"))
    imgs2 = Book.objects.filter(Q(location="takayama") & Q(people="N"))
    imgs3 = Book.objects.filter(Q(location="takayama") & Q(people="C"))
    imgs4 = Book.objects.filter(Q(location="takayama") & Q(people="J"))
    
    return render(request, "users/Takayama.html", {"imgs1" : imgs1, "imgs2" : imgs2, "imgs3" : imgs3, "imgs4" : imgs4 })

def GetTakayama_mov(request):
    logger.info("USER:%s LOAD TAKAYAMA_MOV PAGE", login_user_name)
    #imgs = picture_db.objects.get(location = "Toyama")
    return render(request, "users/Takayama_mov.html")

def GetToyama(request):
    logger.info("USER:%s LOAD TOYAMA PAGE", login_user_name)
    imgs1 = Book.objects.filter(Q(location="toyama") & Q(people="A"))
    imgs2 = Book.objects.filter(Q(location="toyama") & Q(people="N"))
    imgs3 = Book.objects.filter(Q(location="toyama") & Q(people="C"))
    imgs4 = Book.objects.filter(Q(location="toyama") & Q(people="J"))
    #imgs = picture_db.objects.get(location = "Toyama")
    return render(request, "users/Toyama.html", {"imgs1" : imgs1, "imgs2" : imgs2, "imgs3" : imgs3, "imgs4" : imgs4 })

def GetGero(request):
    logger.info("USER:%s LOAD GERO PAGE", login_user_name)
    #imgs = picture_db.objects.get(location = "Gero")
    imgs1 = Book.objects.filter(Q(location="gero") & Q(people="A"))
    imgs2 = Book.objects.filter(Q(location="gero") & Q(people="N"))
    imgs3 = Book.objects.filter(Q(location="gero") & Q(people="C"))
    imgs4 = Book.objects.filter(Q(location="gero") & Q(people="J"))
    #imgs = picture_db.objects.get(location = "Toyama")
    return render(request, "users/Gero.html", {"imgs1" : imgs1, "imgs2" : imgs2, "imgs3" : imgs3, "imgs4" : imgs4 })

def GetBacktoLogin():
    logger.info("USER:%s LOAD NAGOYA PAGE", login_user_name)
    return redirect("user:login")

def GetShirakawago(request):
    logger.info("USER:%s LOAD SHIRAKAWAGO PAGE", login_user_name)
    imgs1 = Book.objects.filter(Q(location="shirakawago") & Q(people="A"))
    imgs2 = Book.objects.filter(Q(location="shirakawago") & Q(people="N"))
    imgs3 = Book.objects.filter(Q(location="shirakawago") & Q(people="C"))
    imgs4 = Book.objects.filter(Q(location="shirakawago") & Q(people="J"))
    #imgs = picture_db.objects.get(location = "Toyama")
    return render(request, "users/Shirakawago.html", {"imgs1" : imgs1, "imgs2" : imgs2, "imgs3" : imgs3, "imgs4" : imgs4 })

def Chubu_view(request):
    logger.info("USER:%s LOAD CHUBU PAGE", login_user_name)
    return render(request, "users/Chubu.html")

def Wrong_view(request):  
    logger.info("USER:%s WRONG PAGE", login_user_name)
    msg = 0
    if msg ==0:
        msg +=1
        return render(request,"users/Wrong.html")
        time.sleep(3)
        
    return redirect("user:login")

def choice_view(request):
    logger.info("USER:%s LOAD TAKAYAMA PIC/MOV CHOICE PAGE", login_user_name)
    return render(request, "users/choice.html")

def choice_gero_view(request):
    logger.info("USER:%s LOAD GERO PIC/MOV CHOICE PAGE", login_user_name)
    return render(request, "users/choice_gero.html")

def choice_nagoya_view(request):
    logger.info("USER:%s LOAD NAGOYA PIC/MOV CHOICE PAGE", login_user_name)
    return render(request, "users/choice_nagoya.html")

def choice_toyama_view(request):
    logger.info("USER:%s LOAD TOYAMA PIC/MOV CHOICE PAGE", login_user_name)
    return render(request, "users/choice_toyama.html")

def choice_shirakawago_view(request):
    logger.info("USER:%s LOAD SHIRAKAWAGO PIC/MOV CHOICE PAGE", login_user_name)
    return render(request, "users/choice_shirakawago.html")
