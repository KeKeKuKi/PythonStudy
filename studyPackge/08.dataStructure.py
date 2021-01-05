'''
             数据结构
'''

'''
  列表
Python中列表是可变的，这是它区别于字符串和元组的最重要的特点，
一句话概括即：列表可以修改，而字符串和元组不能。
以下是 Python 中列表的方法：
方法	               描述
list.append(x)	   把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。
list.extend(L)	   通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。
list.insert(i, x)  在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，
                      例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。
list.remove(x)	   删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。
list.pop([i])	   从列表的指定位置移除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。
                      元素随即从列表中被移除。（方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，你会经常在 Python 库参考手册中遇到这样的标记。）
list.clear()	   移除列表中的所有项，等于del a[ : ]。
list.index(x)	   返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
list.count(x)	   返回 x 在列表中出现的次数。
list.sort()	       对列表中的元素进行排序。
list.reverse()	   倒排列表中的元素。
list.copy()	       返回列表的浅复制，等于a[:]。
'''

'''
将列表当做堆栈使用
列表方法使得列表可以很方便的作为一个堆栈来使用，堆栈作为特定的数据结构，最先进入的元素最后一个被释放（后进先出）,
用 append() 方法可以把一个元素添加到堆栈顶。用不指定索引的 pop() 方法可以把一个元素从堆栈顶释放出来。例如： 
'''

stack = [1, 2, 3, 4, 5]
point = stack.pop()
stack.append(6)
print("stack:", stack)

'''
将列表当作队列使用

也可以把列表当做队列用，只是在队列里第一加入的元素，第一个取出来；但是拿列表用作这样的目的效率不高。
在列表的最后添加或者弹出元素速度快，然而在列表里插入或者从头部弹出速度却不快（因为所有其他的元素都得一个一个地移动）。 
'''

'''
列表推导式

列表推导式提供了从序列创建列表的简单途径。
通常应用程序将一些操作应用于某个序列的每个元素，用其获得的结果作为生成新列表的元素，或者根据确定的判定条件创建子序列。
每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。
返回结果是一个根据表达从其后的 for 和 if 上下文环境中生成出来的列表。
如果希望表达式推导出一个元组，就必须使用括号。 
'''
print("-------------------------------")
list = [1, 2, 3, 4]
list1 = [3*x for x in list]
list2 = [[x, 2*x] for x in list]
print("list1:", list1)
print("list2:", list2)

#出去开始结束空字符
mess = ["  hello", "   kdak   "]
mess = [word.strip() for word in mess]
print("mess:", mess)

#添加判断条件
list3 = [[x, 2*x] for x in list if x > 2]
print("list3:", list3)

#同样的我们可以这样使用
list4 = ["x", "y"]
list5 = [x*y for x in list for y in list4]
print("list5:", list5)

list6 = [str(round(355/113, i)) for i in range(1, 6)]
print("list6:", list6)

#将3*4的矩阵转换为4*3的列表
list7 = [[1,  2,  3,  4],
         [5,  6,  7,  8],
         [9,  10, 11, 12]]
list8 = [[row[i] for row in list7] for i in range(4)]
print("list8:", list8)

'''
del 语句
使用 del 语句可以从一个列表中依索引而不是值来删除一个元素。
这与使用 pop() 返回一个值不同。可以用 del 语句从列表中删除一个切割，
或清空整个列表（我们以前介绍的方法是给该切割赋一个空列表）。
'''
print("-----------------------------")
a = [1, 2, 3, 4, 5, 6, 7, 8]
del a[0]
print("删除第一个元素:\na = ", a)
del a[3:5]
print("删除第3到5之间元素:\na = ", a)
del a[:]
print("删除所有元素:\na = ", a)


'''
集合

集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。
可以用大括号({})创建集合。注意：如果要创建一个空集合，你必须用 set() 而不是 {} ;
后者创建一个空的字典，下一节我们会介绍这个数据结构。
'''
print("--------------------------------")
#自动去除重复元素
baskset = {"hello","asdasd","akkksjad","hello"}
print(baskset)
print("asdasd in baskset:", "asdasd" in baskset)

charArray1 = set('ashdbkanlahfhu')
charArray2 = set('hjhgbsafhei')
print(charArray1-charArray2)
print(charArray1-charArray2)
print("charArray1:", charArray1)
print("charArray2:", charArray2)
print("charArray1 - charArray2:", charArray1 - charArray2)
print("charArray1 | charArray2:", charArray1 | charArray2)
print("charArray1 & charArray2:", charArray1 & charArray2)
print("charArray1 ^ charArray2:", charArray1 ^ charArray2)

'''
字典

另一个非常有用的 Python 内建数据类型是字典。
序列是以连续的整数为索引，与此不同的是，字典以关键字为索引，关键字可以是任意不可变类型，通常用字符串或数值。
理解字典的最佳方式是把它看做无序的键=>值对集合。在同一个字典之内，关键字必须是互不相同。
一对大括号创建一个空的字典：{}。
'''
print("-----------------------------------------")
tel = {'name': 'zhangsan', 'age': 20, 'sex': 0}
print(tel)
print('name:', tel['name'])
del tel['age']
print(tel)
tel['age'] = 22
print(tel)

keys = sorted(tel.keys())
print(keys)
print('name' in tel)

tel2 = {x: x**2 for x in (2, 4, 6)}
print(tel2)


'''
遍历技巧
在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来： 
'''
tel3 = dict(sape=4139, guido=4127, jack=4098)
print(tel3)
for k, v in tel3.items():
    print(k, v, end=', ')
print()
print('----------------------------------------------')

# 同时遍历两个或更多的序列，可以使用 zip() 组合
questions = ["name", 'age', 'sex']
answers = ['张三', '20', '男']

for q, a in zip(questions, answers):
    print(q, '?   ', a, '!')