import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="123456",  # 数据库密码
    database="pythondb"
)

# # 输出所有数据库列表：
# mycursor = mydb.cursor()
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)

# 创建表 主键
mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")
# mycursor.execute("ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# 插入一条数据
# sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
# val = ("BAIDU", "https://www.baidu.com")
# mycursor.execute(sql, val)
# mydb.commit()  # 数据表内容有更新，必须使用到该语句
# print(mycursor.rowcount, "记录插入成功。")

# sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
# val = [
#     ('Google', 'https://www.google.com'),
#     ('Github', 'https://www.github.com'),
#     ('Taobao', 'https://www.taobao.com'),
#     ('stackoverflow', 'https://www.stackoverflow.com/')
# ]
# mycursor.executemany(sql, val)
# mydb.commit()  # 数据表内容有更新，必须使用到该语句
# print(mycursor.rowcount, "记录插入成功。")

# 为了防止数据库查询发生 SQL 注入的攻击，我们可以使用 %s 占位符来转义查询的条件：
# 如果我们想在数据记录插入后，获取该记录的 ID ，可以使用以下代码：
# sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
# val = ("Zhihu", "https://www.zhihu.com")
# mycursor.execute(sql, val)
# mydb.commit()
# print("1 条记录已插入, ID:", mycursor.lastrowid)


# 查询
mycursor.execute("SELECT * FROM sites")
myresult = mycursor.fetchall()  # fetchall() 获取所有记录
for x in myresult:
    print(x)