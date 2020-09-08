from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import *

def hello(request):
    return HttpResponse('hello, world!')


def index_view(request):

    if request.method=='GET':
        return render(request,'register.html')

    else:
        uname=request.POST.get('user')
        upwd=request.POST.get('pwd')
        if uname and upwd:
            stu=Stduent(sname=uname,spwd=upwd)
            stu.save()
            return HttpResponse("注册成功")
        else:
            return HttpResponse("注册失败")




# 处理登录功能
def login_view(request):
    name = request.POST.get('user')
    pwd = request.POST.get('pwd')
    if name == 'myh' and pwd == '123456':
        return HttpResponse('登录成功')
    else:
        return HttpResponse('登录失败')
