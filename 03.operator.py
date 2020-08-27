'''
                                                运算符
Python语言支持以下类型的运算符:
算术运算符
比较（关系）运算符
赋值运算符
逻辑运算符
位运算符
成员运算符
身份运算符
运算符优先级
'''

#Python算术运算符
var1 = 3+3 #加法运算
print("var1 =",var1)
var2 = 5-3 #减法运算
print("var2 =",var2)
var3 = 5*5 #乘法运算
print("var3 =",var3)
var4 = 5/2 #除法运算
print("var4 =",var4)
var5 = 5%2 #求余运算
print("var5 =",var5)
var6 = 5**2 #幂运算
print("var6 =",var6)
var7 = 5//2 #商 向下取整
print("var7 =",var7)
var8 = -5//2 #商 向下取整
print("var8 =",var8)

'''
Python比较运算符
'''
a = 21
b = 10
c = 0
print("------------------------------")
if ( a == b ):
   print ("a 等于 b")
else:
   print ("a 不等于 b")

if ( a != b ):
   print ("a 不等于 b")
else:
   print ("a 等于 b")

if ( a < b ):
   print ("a 小于 b")
else:
   print ("a 大于等于 b")

if ( a > b ):
   print ("a 大于 b")
else:
   print ("a 小于等于 b")

if ( a <= b ):
   print ("a 小于等于 b")
else:
   print ("a 大于  b")

if ( b >= a ):
   print ("b 大于等于 a")
else:
   print ("b 小于 a")


'''
Python赋值运算符
'''
print("------------------------------")
var9 = 2
var9 += 1     #加等于
print("var9:",var9)

var10 = 3
var10 -= 2    #减等于
print("var10:",var10)

var11 = 4
var11 *= 3    #乘等于
print("var11:",var11)

var12 = 5
var12 /= 2    #除等于
print("var12:",var12)

var13 = 6
var13 %= 4   #余等于 等效于 c = c % a
print("var13:",var13)

var14 = 7
var14 **= 2  #幂等于 等效于 c = c ** a
print("var14:",var14)

var15 = 8
var15 //= 3  #等效于 c = c // a
print("var15:",var15)

# var16 = 9
# var16 := 3
# print("var16:",var16)

'''
Python位运算符
按位运算符是把数字看作二进制来进行计算的。Python中的按位运算法则如下：
  a = 00111100
  b = 00001101
  
a&b = 00001100  #与运算 全1则1
a|b = 00111101  #或运算 有1则1
~a  = 11000011  #非运算 取反
a^b = 00110001  #异或运算 不同则1
'''
a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101
c = 0
print("------------------------------")
c = a & b;        # 12 = 0000 1100
print ("c 的值为：", c)

c = a | b;        # 61 = 0011 1101
print ("c 的值为：", c)

c = a ^ b;        # 49 = 0011 0001
print ("c 的值为：", c)

c = ~a;           # -61 = 1100 0011
print ("c 的值为：", c)

c = a << 2;       # 240 = 1111 0000
print ("c 的值为：", c)

c = a >> 2;       # 15 = 0000 1111
print ("c 的值为：", c)

'''
Python逻辑运算符
and	x and y---布尔"与"-----如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	(a and b) 返回 20。
or	x or y----布尔"或"-----如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。	(a or b) 返回 10。
not	not x-----布尔"非"-----如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not(a and b) 返回 False

'''
print("------------------------------")
a = 10
b = 20
print("a:",bool(a))
print("b:",bool(b))
#判断时真假通过bool()方法转化 目前我的认知以为转化时非零为真
if ( a and b ):
   print ("1 - 变量 a 和 b 都为 true")
else:
   print ("1 - 变量 a 和 b 有一个不为 true")

if ( a or b ):
   print ("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
   print ("2 - 变量 a 和 b 都不为 true")
print("------------------------------")
# 修改变量 a 的值
a = 0
print("a:",bool(a))
if ( a and b ):
   print ("3 - 变量 a 和 b 都为 true")
else:
   print ("3 - 变量 a 和 b 有一个不为 true")

if ( a or b ):
   print ("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
   print ("4 - 变量 a 和 b 都不为 true")

if not( a and b ):
   print ("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
   print ("5 - 变量 a 和 b 都为 true")


'''
Python成员运算符
__in______如果在指定的序列中找到值返回 True，否则返回 False。
__not in__如果在指定的序列中没有找到值返回 True，否则返回 False。
'''
print("------------------------------")
list = [1, 2, 3, 4, 5 ]
print("3 in list:",3 in list)
print("7 in list:",7 in list)

'''
Python身份运算符
is	is 是判断两个标识符是不是引用自一个对象
is not	is not 是判断两个标识符是不是引用自不同对象
'''
print("------------------------------")
x = 1
y = x
z = x
print("y is x",y is x)
print("y is z",y is z)

'''
Python运算符优先级

以下表格列出了从最高到最低优先级的所有运算符：
-----------------------------------------------------------------------
运算符	                  描述
-----------------------------------------------------------------------
**	                      指数 (最高优先级)
~ + -	                  按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
* / % //	              乘，除，求余数和取整除
+ -	                      加法减法
>> <<	                  右移，左移运算符
&	                      位 'AND'
^ |	                      位运算符
<= < > >=	              比较运算符
== !=	                  等于运算符
= %= /= //= -= += *= **=  赋值运算符
is is not	              身份运算符
in not in	              成员运算符
not and or	              逻辑运算符
-----------------------------------------------------------------------
'''