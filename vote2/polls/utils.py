import hashlib
import random


def gen_md5_digest(content):
    return hashlib.md5(content.encode()).hexdigest()


print(gen_md5_digest('1qaz2wsx'))
print(gen_md5_digest(('Abc123!!')))


ALL_CHARS = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'


def gen_code(length=4):
    return ''.join(random.choices(ALL_CHARS, k=length))
