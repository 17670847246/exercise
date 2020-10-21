#变量
# =在这里是赋值的意思

a = '你好世界'
a = 'orange' #String 字符串需要用引号包裹
print(a)
b = 32  # Number类型  -> int float long complex
# print(b)
c = False # 布尔类型
# print(c)

# 以上'orange' 32 False 有各自对应的数据类型

print(12)
print(34.22)
print(2**10) #写法complex类型，结果int类型

# z = x+yj x是
print(1+4j)
print(complex(7+8j))
#形如 z = x+yj 统称为复数 **也是

#布尔类型 用来表示真假 或者 对错  一共就是 True 和 False

print(True) #True
print(2>1)  #True
print(False) #False
print(1>2)   #False
print(type(True))

#列表 list    常用

names = ['赵白石', '王世均', 234, True]
print(type(names))

#字典 dict    常用

dict1 = {'name': '赵白石', 'sex': 'man'}
print(type(dict1))

#元祖 tuple   常用

nums = (1, 2, 5, 56, 23)
print(nums)
print(type(nums))

#集合类型 set
x = {10, 'ijoag', False, 'good'}
print(x)

