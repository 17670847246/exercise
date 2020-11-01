import json
import random

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from polls.captcha import Captcha
from polls.models import Subject, Teachers, User
from polls.utils import gen_code, gen_md5_digest


def show_index(request):
    # 从数据库中获取数据
    fruits = ['Apple', 'Orange', 'Pitaya', 'Durian', 'Waxberry', 'Blueberry',
              'Grape', 'Peach', 'Pear', 'Banana', 'Watermelon', 'Mango'
    ]
    selected_fruits = random.sample(fruits, 3)
    # render函数可以实现对模板页的渲染，它有三个参数分别是：
    #  - 第一个参数：request：请求对象
    #  - 第二个参数：需要渲染的模板页（index.html)
    #  - 第三个参数：渲染页面时需要用到的数据（字典）
    return render(request, 'index.html', {
        'fruits':selected_fruits,
        'greeting': '劝君更近一杯酒'
    })

# 视图函数（接收来自浏览器的用户请求，然后返回一个响应对象输出到用户浏览器）
def show_subjects(request:HttpResponse):
    # QuerSet ---> 容器
    subjects = Subject.objects.all().order_by('no')
    return render(request, 'subjects.html',{
        'subjects': subjects
    })


def show_teachers(request: HttpResponse) -> HttpResponse:
    try:
        sno = int(request.GET.get('sno'))
        teachers = []
        if sno:
            # QuerySet
            subject = Subject.objects.only('name').get(no=sno)
            teachers = Teachers.objects.filter(subject=subject).order_by('no')
        return render(request, 'teachers.html',{
            'teachers': teachers,
            'subject': subject
        })
    except (ValueError, Subject.DoesNotExist):
        return redirect('/')    # redirect 重定向


def praise_or_criticize(request:HttpResponse) -> HttpResponse:
    try:
        tno = int(request.GET.get('tno'))
        teacher = Teachers.objects.get(no=tno)
        if request.path.startswith('/praise/'):
            teacher.good_count += 1
            count = teacher.good_count
        else:
            teacher.bad_count += 1
            count = teacher.bad_count
        teacher.save()
        data = {'code': 8888, 'mesg': '投票成功', 'count': count}
    except ValueError:
        data = {'code': 9999, 'mesg': '投票失败'}
    # json.dumps(data)  dict --> str
    # return  HttpResponse(json.dumps(data), content_type='application/json; charset=utf8')
    return JsonResponse(data)


def get_captcha(request: HttpResponse) -> HttpResponse:
    code = gen_code()
    image_data = Captcha.instance().generate(code)
    return HttpResponse(image_data, content_type='image/png')


def login(request:HttpResponse) -> HttpResponse:
    """登入"""
    hint = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            password = gen_md5_digest(password)
            user = User.objects.filter(username=username, password=password).first()
            if user:
                pass
            else:
                hint = '用户或密码错误'
        else:
            hint = '请输入有效的用户名'
    return render(request, 'login.html', {
        'hint': hint
    })


def register(request: HttpResponse) -> HttpResponse:
    """注册"""
    if request.method == 'POST':
        pass
    return render(request, 'register.html')
