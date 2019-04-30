
import psycopg2

print("111")

conn = psycopg2.connect(database ="ivs",user="lynxi",password="lynxi",host="localhost",port="5432")
cur = conn.cursor()
# cur.execute("CREATE TABLE student(id integer,name varchar,sex varchar);")

# 插入数据
cur.execute("INSERT INTO student(id,name,sex)VALUES(%s,%s,%s)", (1, 'Aspirin', 'M'))
cur.execute("INSERT INTO student(id,name,sex)VALUES(%s,%s,%s)", (2, 'Taxol', 'F'))
cur.execute("INSERT INTO student(id,name,sex)VALUES(%s,%s,%s)", (3, 'Dixheral', 'M'))

# 获取结果
cur.execute('SELECT * FROM student')

one = cur.fetchone()
print(one)
x = one[1]
print(x), type(x), repr(x)

results = cur.fetchall()
print(results)
for res in results:
    num = str(res[0])
    resstr =num +","+res[1]+","+res[2]
    print(resstr)



# 关闭练级
conn.commit()
cur.close()
conn.close()
