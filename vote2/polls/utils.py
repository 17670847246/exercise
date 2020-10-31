import hashlib


def gen_md5_digest(content):
    return hashlib.md5(content.encode()).hexdigest()


print(gen_md5_digest('1qaz2wsx'))
print(gen_md5_digest(('Abc123!!')))