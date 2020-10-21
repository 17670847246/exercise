



# python 中的for
#range 生成指定区间的整数序列 [列表]
#range(1,11) [1,2,3,4,5,6,7,8,9,10]

# for i in range(1,11):
#     print(i)
#
#
# for x in 'hello world':
#     print(x)
#
#
# for y in 10:
#     print(y) #10不是一个可迭代的对象 所以报错


sum = 0
for x in range(1, 101): #包含0 不包含101
    sum += x

print(sum)



