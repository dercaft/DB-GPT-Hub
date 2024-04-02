import sqlite3

# 定义查询语句
query = """
select a.购买人数 / b.购买人数 from ( select 购买人数 from 图书与平台 where 书名id = 'item_book.2_2_17' and 平台id = 'item_book.2_2_13' ) a , ( select sum ( 购买人数 ) as 购买人数 from 图书与平台 where 书名id = 'item_book.2_2_17' ) b
"""



# 连接到数据库
db_path = "/data/lcy/elec/DB-GPT-Hub/dbgpt_hub/data/DuSQL/database/购书平台/购书平台.sqlite"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

try:
    # 执行查询
    cursor.execute(query)

    # 获取结果
    rows = cursor.fetchall()
    print("Query executed successfully. Results:")
    for row in rows:
        print(row)

except sqlite3.Error as e:
    # 捕获并打印错误信息
    print("Error executing query:", e)
    # 打印表格信息
    cursor.execute("PRAGMA table_info(各省财政收入)")
    print(cursor.fetchall())
    

finally:
    # 关闭数据库连接
    conn.close()
