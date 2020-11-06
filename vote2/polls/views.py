
import random
from urllib.parse import unquote


from django.db import DatabaseError
from django.db.models import Q
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.shortcuts import render, redirect

from polls.captcha import Captcha
from polls.models import Subject, Teachers, User
from polls.utils import gen_code, gen_md5_digest, send_message_by_sms, random_mobile_code, check_username,  check_password


def show_index(request: HttpRequest) -> HttpResponse:
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
def show_subjects(request:HttpRequest):
    # QuerSet ---> 容器
    subjects = Subject.objects.all().order_by('no')
    return render(request, 'subjects.html',{
        'subjects': subjects
    })


def show_teachers(request: HttpRequest) -> HttpResponse:
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


def praise_or_criticize(request:HttpRequest) -> HttpResponse:
    if request.session.get('userid'):
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
    else:
        data = {'code': 20002, 'mesg': '请先登入'}
    # json.dumps(data)  dict --> str
    # return  HttpResponse(json.dumps(data), content_type='application/json; charset=utf8')
    return JsonResponse(data)


def get_captcha(request: HttpRequest) -> HttpResponse:
    """生成验证码图片"""
    code = gen_code()
    request.session['captcha'] = code.lower()
    image_data = Captcha.instance().generate(code)
    return HttpResponse(image_data, content_type='image/png')


def login(request:HttpRequest) -> HttpResponse:
    """登入"""
    hint = request.GET.get('hint') or ''
    returnurl = request.GET.get('returnurl', '/')
    if returnurl != '/':
        # 将百分号编码还原原始的字符串
        returnurl = unquote(returnurl)
    if request.method == 'POST':
        returnurl = request.POST.get('returnurl', '/')
        captcha_from_serv = request.session.get('captcha', '0')
        captcha_from_user = request.POST.get('captcha', '1').lower()
        if captcha_from_serv == captcha_from_user:
            username = request.POST.get('username')
            password = request.POST.get('password')
            if check_username(username) and check_password(password):
                password = gen_md5_digest(password)
                user = User.objects.filter(Q(username=username) | Q(tel=username)).filter(password=password).first()
                if user:
                    request.session['userid'] = user.no
                    request.session['username'] = user.username
                    return redirect(returnurl)
                else:
                    hint = '用户或密码错误'
            else:
                hint = '请输入有效的用户名'
        else:
            hint = '请输入有效的验证码'
    return render(request, 'login.html', {'hint': hint, 'returnurl': returnurl})


def register(request: HttpRequest) -> HttpResponse:
    """注册"""
    hint = ''
    if request.method == 'POST':
        agreement = request.POST.get('agreement')
        if agreement == 'on':
            code_from_user = request.POST.get('mobilecode','0')
            code_from_sess = request.session.get('mobilecode','1')
            if code_from_user == code_from_sess:
                username = request.POST.get('username')
                password = request.POST.get('password')
                tel = request.POST.get('tel')
                if check_username(username):
                    if check_password(password):
                        if tel:
                            user = User()
                            user.username = username
                            user.password = gen_md5_digest(password)
                            user.tel = tel
                            try:
                                user.save()
                            except DatabaseError:
                                hint = '用户或手机号已被注册，请尝试其他的用户名或手机号'
                            else:
                                hint = '注册成功,请登录'
                                return redirect(f'/login/?hint={hint}')
                        else:
                            hint = '电话号码错误'
                    else:
                        hint = '密码少于8位'
                else:
                    hint = '用户名少于6位数'
            else:
                hint = '请输入正确的手机验证码'
        else:
            hint = '请勾选同意网站用户协议及隐私政策'
    return render(request, 'register.html', {'hint': hint})


def logout(request: HttpRequest) -> HttpResponse:
    request.session.flush()
    return redirect('/')


def send_mobile_code(request: HttpRequest, tel) -> HttpResponse:
    code = random_mobile_code()
    request.session['mobilecode'] = code
    message = f'你的短信验证码为{code},【铁壳测试】'
    send_message_by_sms(tel=tel, message=message)
    return JsonResponse({'code': 20000, 'message': '短信验证码已经发送到您的手机'})

def is_unique_username(request: HttpRequest) -> HttpResponse:
    """检查用户名唯一性"""
    username = request.GET.get('username')
    if check_username(username):
        if User.objects.filter(username=username).exists():
            data = {'code': 30001, 'message': '用户名已被注册'}
        else:
            data = {'code': 30000, 'message': '用户名可以使用'}
    else:
        data = {'code': 30002, 'message': '无效的用户名'}
    return JsonResponse(data)













