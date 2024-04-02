import os
import sqlite3

def create_sqlite_from_sql(schema_file, sqlite_file):
    # 读取 SQL 文件内容
    with open(schema_file, 'r') as f:
        sql_script = f.read()

    # 连接到 SQLite 数据库，执行 SQL 脚本
    conn = sqlite3.connect(sqlite_file)
    cursor = conn.cursor()
    cursor.executescript(sql_script)
    conn.commit()
    conn.close()

def main():
    # 获取database文件夹下的所有文件夹
    os.chdir('../database')
    folders = [name for name in os.listdir('.') if os.path.isdir(name)]

    for folder in folders:
        schema_file = os.path.join(folder, 'schema.sql')
        sqlite_file = os.path.join(folder, folder + '.sqlite')
        # 如果 sqlite_file 存在则删除
        if os.path.exists(sqlite_file):
            # continue
            os.remove(sqlite_file)
        print(f"正在处理 '{folder}' 数据库...")
        # 如果 schema.sql 存在则创建对应的 SQLite 文件
        if os.path.exists(schema_file):
            create_sqlite_from_sql(schema_file, sqlite_file)
            print(f"SQLite 文件 '{sqlite_file}' 创建成功！")

if __name__ == "__main__":
    main()
