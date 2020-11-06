import hashlib
import random
import re

import requests

ALL_CHARS = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'


def gen_code(length=4):
    return ''.join(random.choices(ALL_CHARS, k=length))


def gen_md5_digest(content):
    return hashlib.md5(content.encode()).hexdigest()


def random_mobile_code(length=6):
    return ''.join(random.choices('1234567890', k=length))


def send_message_by_sms(*, tel, message):
    resp = requests.post(
        url='http://sms-api.luosimao.com/v1/send.json',
        auth=('api', 'key-18e75c7490a95cfc2f01afda4378dbb0'),
        data={
            'mobile': tel,
            'message': message
        }, timeout=3, verify=False)
    return resp.json()


USERNAME_PATTERN = re.compile(r'[0-9a-zA-Z_]{6,20}')  # == (r'\w{6,20}')


def check_username(username):
    """检查用户名"""
    return USERNAME_PATTERN.fullmatch(username) is not None


def check_password(password):
    """检查密码"""
    return len(password) >= 8



