

c = int(input('请输入世纪'))
y = int(input('请输入年份'))
m = int(input('请输入月份'))

c = c//4-2*c
y = y+(y//4)
m = 13*(m+1)//5
W = (c + y + m ) % 7
print(W)
