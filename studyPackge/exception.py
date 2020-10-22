'''
Python3 错误和异常
作为 Python 初学者，在刚学习 Python 编程时，经常会看到一些报错信息，在前面我们没有提及，这章节我们会专门介绍。
Python 有两种错误很容易辨认：语法错误和异常。
Python assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。
'''
'''
异常处理
try/except
异常捕捉可以使用 try/except 语句。
'''
while True:
    try:
        x = int(input("请输入一个数字: "))
        break
    except ValueError:
        print("您输入的不是数字，请再次尝试输入！")

'''
try 语句按照如下方式工作；
    首先，执行 try 子句（在关键字 try 和关键字 except 之间的语句）。
    如果没有异常发生，忽略 except 子句，try 子句执行后结束。
    如果在执行 try 子句的过程中发生了异常，那么 try 子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，那么对应的 except 子句将被执行。
    如果一个异常没有与任何的 except 匹配，那么这个异常将会传递给上层的 try 中。
一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。
处理程序将只针对对应的 try 子句中的异常进行处理，而不是其他的 try 的处理程序中的异常。
一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组，例如: 
'''
import sys
try:
    f = open('hello.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

'''
try/except...else
try/except 语句还有一个可选的 else 子句，如果使用这个子句，那么必须放在所有的 except 子句之后。
else 子句将在 try 子句没有发生任何异常的时候执行。
使用 else 子句比把所有的语句都放在 try 子句里面要好，这样可以避免一些意想不到，而 except 又无法捕获的异常。
'''

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

'''
try-finally 语句
try-finally 语句无论是否发生异常都将执行最后的代码。
'''
try:
    print("do some thing")
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('这句话，无论异常是否发生都会执行。')

'''
抛出异常
Python 使用 raise 语句抛出一个指定的异常。
raise语法格式如下：
raise [Exception [, args [, traceback]]]
'''
x = 10
if x > 5:
    raise Exception('x 不能大于 5。x 的值为: {}'.format(x))