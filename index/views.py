from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.
def remark_views(request):
    form = RrmarkForm()
    return render(request, '04_remark.html', locals())
def userLogin_views(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, '05_login.html',locals())
    else:
        form = LoginForm(request.POST)
        # uname = request.POST['uname']
        # upwd = request.POST['upwd']
        if form .is_valid():
            cd = form.cleaned_data
            print(cd)
            print(request.POST)
            uname = cd['uname']
            upwd = cd['upwd']
            uList = User.objects.filter(uname=uname,upwd=upwd)
        if uList:
            return HttpResponse('登录成功')
        else:
            form = LoginForm()
            errMsg = '用户名或密码不正确'
            return render(request, '05_login.html', locals())
def register_views(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, '06_register.html', locals())
    else:
        print(request.POST)
        form = RegisterForm(request.POST)
        if form.is_valid():
            User(**form.cleaned_data).save()
            return HttpResponse('注册成功')
        else:
            form = RegisterForm()
            errMsg = '用户名或密码不正确'
            return render(request, '05_login.html', locals())
def loginform_views(request):
    if request.method == 'GET':
        form = UserLoginForm()
        return render(request, '07_login.html', locals())
def widget1_views(request):
    form = WidgetForm()
    return render(request, '09_widget.html', locals())
def cookie1_views(request):
    resp = HttpResponse('添加cookies成功')
    resp.set_cookie('uid','1001',60*60*24*366)
    print(resp)
    return resp
def cookie2_views(request):
    resp = HttpResponseRedirect('/10_login/')
    resp.set_cookie('uname','zsf',60*60*24*31)
    return resp
def login15_views(request):
    if request.method == 'GET':
        if 'uid' in request.session and 'uname' in request.session:
            uid = request.session['uid']
            uname = request.session['uname']
            return render(request,'11_index.html',locals())
        # form = WidgetForm()
        return render(request, '10_login.html', locals())
    else:
        uname = request.POST['uname']
        upwd = request.POST['upwd']
        uList = User.objects.filter(uname=uname,upwd=upwd)
        if uList:
            resp = render(request, '11_index.html')
            if 'isSaved' in request.POST:
                print(request.POST)
                uid = uList[0].id
                expires = 60*60*24*366
                resp.set_cookie('uid', uid, expires)
                resp.set_cookie('uname', uname, expires)
            return resp
        else:
            form = WidgetForm()
            return render(request,'11_index.html',locals())
def getcookie_views(request):
    print(request.COOKIES)
    # print(request.COOKIES['uid'])
    # print(request.COOKIES['uname'])
    return HttpResponse('ok')
def index_views(request):
    print('hello')
    return render(request,'11_index.html')

