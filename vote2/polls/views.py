import random

from django.http import HttpResponse
from django.shortcuts import render, redirect

from polls.models import Subject, Teachers


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


def praise(request:HttpResponse) -> HttpResponse:
    try:
        sno = request.GET.get('sno')
        tno = request.GET.get('tno')
        teacher = Teachers.objects.get(no=tno)
        teacher.good_count += 1
        teacher.save()
        return redirect(f'/teachers/?sno={sno}')
    except ValueError:
        return redirect('/')

def bad(request:HttpResponse) -> HttpResponse:
    try:
        sno = request.GET.get('sno')
        tno = request.GET.get('tno')
        teacher = Teachers.objects.get(no=tno)
        teacher.bad_count += 1
        teacher.save()
        return redirect(f'/teachers/?sno={sno}')
    except ValueError:
        return redirect('/')
