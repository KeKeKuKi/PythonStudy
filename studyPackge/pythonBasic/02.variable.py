'''
变量赋值
Python 中的变量赋值不需要类型声明。
每个变量在内存中创建，都包括变量的标识，名称和数据这些信息。
每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
等号（=）用来给变量赋值。
等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。例如：
'''

counter = 100 # 整型
miles = 100.01 # 浮点型
name = "Tom" # 字符串

# Python允许你同时为多个变量赋值。例如：
a = b = c = 1
e, f, g = 1, 1.0, 'str'
dict = {'name': 'zs', 'sex': '男'}

set = {1, 2.0, 'str', 'str'}
list = [1, 2.0, 'str', 'str', dict]
yu = (1, 2.0, 'str', 'str')

print("list：", list)
print("set:", set)
print("yu：", yu)

print("dict:", dict)
'''
Python 数据类型

Python 定义了一些标准类型，用于存储各种类型的数据。
Python有五个标准的数据类型：
Numbers（数字）
String（字符串）
List（列表）
Tuple（元组）
Dictionary（字典）
'''
'''
数字数据类型用于存储数值。
Python支持四种不同的数字类型：
int（有符号整型）
long（长整型[也可以代表八进制和十六进制]）
float（浮点型）
complex（复数）
他们是不可改变的数据类型，这意味着改变数字数据类型会分配一个新的对象。
当你指定一个值时，Number对象就会被创建：
'''
var1 = 1
var2 = 2.0

#您也可以使用del语句删除一些对象的引用。
#del语句的语法是：del var1[,var2[,var3[....,varN]]]]
del var1, var2

'''
python 不再支持Long类型 合并到了int类型
Python 还支持复数，复数由实数部分和虚数部分构成，可以用 a + bj,或者 complex(a,b) 表示， 复数的实部 a 和虚部 b 都是浮点型。
'''
var3 = 1 + 1j #复数
var4 = complex(1, 1) #复数
flage = var3 == var4
print(type(flage))
print("-----------------------------------------")
print("var3 == var4 : ", flage)

'''
Python字符串
字符串或串(String)是由数字、字母、下划线组成的一串字符。
一般记为 :
s="1aa2···an"(n>=0)
它是编程语言中表示文本的数据类型。
python的字串列表有2种取值顺序:
从左到右索引默认0开始的，最大范围是字符串长度少1
从右到左索引默认-1开始的，最大范围是字符串开头
例如：
var = 'hello'
 h  e  l  l  o
 0  1  2  3  4
-5 -4 -3 -2 -1

如果你要实现从字符串中获取一段子字符串的话，可以使用 [头下标:尾下标] 来截取相应的字符串，
其中下标是从 0 开始算起，可以是正数或负数，下标可以为空表示取到头或尾。
[头下标:尾下标] 获取的子字符串包含头下标的字符，但不包含尾下标的字符。
'''
strxxx = 'abcde'
print(strxxx[-4])
var5 = "abcdefgh"[0:5]
var6 = "abcdefgh"[-8:-5]
print("-----------------------------------------")
print("var5:", var5)
print("var6:", var6)
#Python 列表截取可以接收第三个参数，参数作用是截取的步长，以下实例在索引 0 到索引 5 的位置并设置为步长为 2（间隔）来截取字符串：

var7 = "abcdef"[0:5:3]
print("var7:", var7)

'''
Python列表
List（列表） 是 Python 中使用最频繁的数据类型。
列表可以完成大多数集合类的数据结构实现。
它支持字符，数字，字符串甚至可以包含列表（即嵌套）。
列表用 [ ] 标识，是 python 最通用的复合数据类型。
列表中值的切割也可以用到变量 [头下标:尾下标] ，就可以截取相应的列表，
从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可以为空表示取到头或尾。

var t = ['a','b','c','d','e']

['a','b','c','d','e']
  0   1   2   3   4
 -5  -4  -3  -2  -1
  
'''
list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']
print("-----------------------------------------")
print(list)  # 输出完整列表
print(list[0])  # 输出列表的第一个元素
print(list[1:3]) # 输出第二个至第三个元素
print(list[2:])  # 输出从第三个开始至列表末尾的所有元素
print(tinylist * 2)  # 输出列表
print(list + tinylist)  # 打印组合的列表

'''
Python 字典
字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。
两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
'''
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'runoob', 'code': 6734, 'dept': 'sales'}
print("-----------------------------------------")
print(dict['one'])          # 输出键为'one' 的值
print(dict[2])              # 输出键为 2 的值
print(tinydict)             # 输出完整的字典
print(tinydict.keys())      # 输出所有键
print(tinydict.values())    # 输出所有值

'''
Python数据类型转换
有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。
以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。
'''
print("-----------------------------------------")
x = "1010"
var8 = int(x, 2) # 第二个参数为x的进制
print("var8:", var8)

var9 = int(x, 10)
print("var9:", var9)

var10 = float(x) #转化为浮点型
print("var10:", var10)

var11 = complex(1, 1)
print("var11:", var11)

var12 = str(11)
print("var12:",var12)

var13 = repr({'one' : 1, 'two' : 2}) #转换为表达式字符串
print("var13:", var13)

var14 = chr(11110) #转换为字符
print("var14:", var14)

var15 = tuple({1: 2, 3: 4}) #转化为元组 （字典会返回key组成的元组）
print("var15:",var15)

# aTuple = (123, 'xyz', 'zzz', 'abc');
# aList = list(aTuple)
# print ("列表元素 : ", aList)


#更多参考帮助文档.pdf



