'''
输出格式美化

Python两种输出值的方式: 表达式语句和 print() 函数。
第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用。
如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
    str()： 函数返回一个用户易读的表达形式。
    repr()： 产生一个解释器易读的表达形式。
'''
import math

hello = 'hello'
print("易于人识别：", str(hello))
print("易于机器识别：", repr(hello))

number = 1/7
print("易于人识别：", str(number))
print("易于机器识别：", repr(number))

# 格式控制，以下两种方式输出次方表
for x in range(1, 5):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # 注意前一行 'end' 的使用
    print(repr(x*x*x).rjust(4))
print("==============")
for x in range(1, 5):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
'''
注意：在第一个例子中, 每列间的空格由 print() 添加。
这个例子展示了字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。
还有类似的方法, 如 ljust() 和 center()。 这些方法并不会写任何东西, 它们仅仅返回新的字符串。
另一个方法 zfill(), 它会在数字的左边填充 0，如下所示：
'''
# format基本用法
print('{0}网址： "{1}!"'.format('菜鸟教程', 'www.runoob.com'))
# 参数式
print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))
# 任意结合
print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))
# !a (使用 ascii()), !s (使用 str()) 和 !r (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
print('常量 PI 的值近似为： {!r}'.format(math.pi))
# 可选项 : 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化.
print('常量 PI 的值近似为 {0:.3f}'.format(math.pi))
# 在 : 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
  print('{0:10} ==> {1:10d}'.format(name, number))
# % 操作符也可以实现字符串格式化。
# 它将左边的参数作为类似 sprintf() 式的格式化字符串, 而将右边的代入, 然后返回格式化后的字符串.
print('常量 PI 的值近似为：%5.3f。' % math.pi)

'''
读取键盘输入
Python提供了 input() 内置函数从标准输入读入一行文本，默认的标准输入是键盘。
input 可以接收一个Python表达式作为输入，并将运算结果返回。 
'''
print('---------------------------------')
input = input("请输入：")
print ("你输入的内容是: ", input, "(将写入后面示例的文件！)")

'''
读和写文件
open() 将会返回一个 file 对象，基本语法格式如下: 
'''
file = open('hello.txt', 'a+')
file.write(input)
file.close()

file = open('hello.txt', 'r')
text = file.read()
line = file.readline()
print("文件内容：", text)
print("再读一行内容：", line)
file.close()
print('------------------------------')
file = open('hello.txt', 'r')
for line in file:
    print("循环读取：",line)
# filename：包含了你要访问的文件名称的字符串值。
# mode：决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
'''
不同模式打开文件的完全列表：
模式	描述
r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。
r+	打开一个文件用于读写。文件指针将会放在文件的开头。
rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
'''

'''
f.write(string) 将 string 写入到文件中, 然后返回写入的字符数。 
'''
print("-------------------------------------")
f = open("hello.txt", "w")
num = f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
print("写入了{}个字符".format(num))
# 关闭打开的文件
f.close()

'''
f.tell()
f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。
f.seek()
如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。
from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如：
    seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
    seek(x,1) ： 表示从当前位置往后移动x个字符
    seek(-x,2)：表示从文件的结尾往前移动x个字符 
'''

'''
pickle 模块

python的pickle模块实现了基本的数据序列和反序列化。

通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。

通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。

基本接口：

pickle.dump(obj, file, [,protocol])

有了 pickle 这个对象, 就能对 file 以读取的形式打开:

x = pickle.load(file)

注解：从 file 中读取一个字符串，并将它重构为原来的python对象。

file: 类文件对象，有read()和readline()接口。
'''
print('----------------------------------')
#!/usr/bin/python3
import pickle,pprint
# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}
selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)
output = open('data.pkl', 'wb')
# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)
output.close()

#使用pickle模块从文件中重构python对象
pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()