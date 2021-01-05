import pymysql

# 打开数据库连接
db = pymysql.connect("127.0.0.1", "root", "123456", "pythondb")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# # 使用 execute()  方法执行 SQL 查询
# cursor.execute("SELECT * from sites")
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
# print(data)
# # 关闭数据库连接
# db.close()

# 插入数据
# SQL 插入语句
# sql = """INSERT INTO sites (name, url) VALUES ('Mac', 'www.jhasj.com')"""
# try:
#     # 执行sql语句
#     cursor.execute(sql)
#     # 提交到数据库执行
#     db.commit()
#     print("插入成功！")
# except:
#     # 如果发生错误则回滚
#     print("插入失败！")
#     db.rollback()
# # 关闭数据库连接
# db.close()

# 以上例子也可以写成如下形式：
# SQL 插入语句
# sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
#        LAST_NAME, AGE, SEX, INCOME) \
#        VALUES ('%s', '%s',  %s,  '%s',  %s)" % \
#        ('Mac', 'Mohan', 20, 'M', 2000)

# SQL 查询语句
# sql = "SELECT * FROM sites \
#        WHERE id > %s" % (3)
# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 获取所有记录列表
#    results = cursor.fetchall()
#    for row in results:
#       name = row[0]
#       url = row[1]
#       id = row[2]
#        # 打印结果
#       print ("name=%s,url=%s,id=%s" % \
#              (name, url, id))
# except:
#    print ("Error: unable to fetch data")

'''
执行事务

事务机制可以确保数据一致性。

事务应该具有4个属性：原子性、一致性、隔离性、持久性。这四个属性通常称为ACID特性。

    原子性（atomicity）。一个事务是一个不可分割的工作单位，事务中包括的诸操作要么都做，要么都不做。
    一致性（consistency）。事务必须是使数据库从一个一致性状态变到另一个一致性状态。一致性与原子性是密切相关的。
    隔离性（isolation）。一个事务的执行不能被其他事务干扰。即一个事务内部的操作及使用的数据对并发的其他事务是隔离的，并发执行的各个事务之间不能互相干扰。
    持久性（durability）。持续性也称永久性（permanence），指一个事务一旦提交，它对数据库中数据的改变就应该是永久性的。接下来的其他操作或故障不应该对其有任何影响。 

Python DB API 2.0 的事务提供了两个方法 commit 或 rollback。

对于支持事务的数据库， 在Python数据库编程中，当游标建立之时，就自动开始了一个隐形的数据库事务。

commit()方法游标的所有更新操作，rollback（）方法回滚当前游标的所有操作。每一个方法都开始了一个新的事务。
'''