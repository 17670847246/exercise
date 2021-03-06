"""vote2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from polls.views import show_subjects, show_teachers, praise_or_criticize, login, register, get_captcha, logout, \
    send_mobile_code, is_unique_username

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_subjects),
    path('teachers/', show_teachers),
    path('praise/', praise_or_criticize),
    path('bad/', praise_or_criticize),
    path('login/', login),
    path('logout/', logout),
    path('register/', register),
    path('captcha/', get_captcha),
    # /mobile/?tel=31423432515
    # path('mobile/', send_mobile_code),
    # /mobile/3153253125/
    path('mobile/<str:tel>/', send_mobile_code),
    path('check/', is_unique_username)
]

