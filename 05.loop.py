'''
循环语句
Python 中的循环语句有 for 和 while。
'''

'''
while 循环
Python 中 while 语句的一般形式：
while 判断条件(condition)：
    执行语句(statements)……
    
在 while … else 在条件语句为 false 时执行 else 的语句块。
'''
count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")

'''
for 语句
Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
for循环的一般格式如下：
for <variable> in <sequence>:
    <statements>
else:
    <statements>
'''
print("-------------------------")
for i in range(5):
    print(i)

'''
使用循环做一个99乘法表
'''
print("-------------------------")
print("99乘法表")
print("-------------------------")
tip = 1
for x in range(1,10):
    y = 1
    while y <= tip:
        print(y,"*",x,"=",x * y, end='   ')
        y += 1
    else:
        print()
        tip += 1

'''
使用循环做一个费布拉契数列
'''
print("-------------------------")
print("费布拉契数列")
print("-------------------------")
one, two = 0, 1
while two in range(1000):
    print(one,end=" ")
    one, two = two, two+one  #注意赋值的先后机制
else:
    print(one)