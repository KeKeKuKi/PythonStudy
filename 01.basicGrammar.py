#单行注释

'''
多行注释
'''

#输入
# input = raw_input("按下 enter 键退出，其他任意键显示...\n")

#输出
#print 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号
print(input)
print("不换行","换行")

#多条语句使用分号分隔
import sys;x = 'hello';sys.stdout.write(x+'\n')

'''
缩进相同的一组语句构成一个代码块，我们称之代码组。
像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
我们将首行及后面的代码组称为一个子句(clause)。
如下实例：
'''

#严格代码缩进
flage = 1
if flage == 1:
    print("1")
elif flage == 2:
    print("2")
else:
    print("3")

