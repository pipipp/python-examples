# -*- coding:utf-8 -*-
import pymysql

__author__ = 'Evan'


def mysql_handle(host='localhost', user='root', password='', port=3306):
    """
    连接Mysql客户端
    :param host: Mysql database name
    :param user: Login username
    :param password: Login password
    :param port: Connection port
    :return:
    """
    # 连接Mysql客户端
    db = pymysql.connect(host=host, user=user, password=password, port=port, db='example')
    cursor = db.cursor()  # 获取一个句柄
    print('连接Mysql成功')

    # 创建表users（如果存在则不创建）
    create_table = 'users'
    create_keys = 'uid INTEGER, pid INTEGER'
    sql = "CREATE TABLE if not exists {0}({1})".format(create_table, create_keys)  # 动态创建数据表
    cursor.execute(sql)

    data = {
        'uid': 6,
        'pid': 8
    }

    # 插入数据到users表
    table = 'users'
    keys = ', '.join(data.keys())
    values = ', '.join(['%s'] * len(data))
    sql = "INSERT INTO {0}({1}) values({2})".format(table, keys, values)  # 动态插入数据表
    cursor.execute(sql, tuple(data.values()))

    # 更新users表中数据
    table = 'users'
    condition = 'uid = %s WHERE pid = %s'
    sql = "UPDATE {0} SET {1}".format(table, condition)  # 动态更新数据表
    cursor.execute(sql, (66, 8))

    # 查询users表中数据
    table = 'users'
    condition = 'uid > 10'
    sql = "SELECT * FROM {} WHERE {}".format(table, condition)  # 动态查询数据表中数据
    cursor.execute(sql)
    print(cursor.rowcount)  # # 查看匹配个数
    print(cursor.fetchone())  # 获取结果的第一条数据，返回一个元组
    print(cursor.fetchall())  # 获取结果的所有数据，返回一个元组，数据量大时会占用很大内存，所以尽量使用fetchone逐条获取

    # 删除users表中数据
    table = 'users'
    condition = 'uid > 10'
    sql = "DELETE FROM {0} WHERE {1}".format(table, condition)  # 动态删除数据表中数据
    cursor.execute(sql)

    # 提交数据（只有提交之后，所有的操作才会生效）
    db.commit()
    # 数据回滚，相当于本次操作什么都没有发生过
    db.rollback()
    # 关闭句柄
    cursor.close()
    db.close()

    # 标准写法
    # try:
    #     cursor.execute(sql)
    #     db.commit()
    # except Exception as ex:
    #     print('Error: {}'.format(ex))
    #     db.rollback()
    # finally:
    #     db.close()


if __name__ == '__main__':
    mysql_handle()
