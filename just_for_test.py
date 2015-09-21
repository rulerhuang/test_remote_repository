#!/usr/bin/env python
#encoding=utf-8

"""
    pg数据库操作的API

    Date: 2014-09
    Author: knktc
    Reviser: alen 2015-08-07 修复了一个bug
             bob  2015-08-31 调整了代码格式
"""

import os
import sys
import traceback
from pprint import pprint

# 第三方包
import psycopg2

# 自定义模块
import conf
from tmtuil import tools


class PostgresClient(object):
    """
        A class for postgres client
    """
    def __init__(self, host='localhost',
                        port=5432,
                        user='user',
                        password='password',
                        database='database'):
        """
            init function ,create db connection

            Args:
                    host ip
                    port 端口号
                    user 用户名
                    password 密码
                    database 数据库名称

            Returns:
                    None
        """
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        # alter by huang on 2015-08-31 for 圆括号隐式换行
        self.conn_string = ("host=%s port=%s user=%s password=%s dbname=%s"
                                %(self.host, self.port, self.user, self.password, self.database)
                            )
        self.conn = psycopg2.connect(self.conn_string)


    def create_cursor(self):
        """
            create cursor
        """
        self.cursor = self.conn.cursor()


    def close_cursor(self):
        """
            close cursor
        """
        self.cursor.close()


    def query(self, query_sql, query_dict):
        """
            user sql string to query data

            Args:
                    query_sql   查询语句
                    query_dict  数据字典

            Returns:
                    True or False,sql_result
        """

        sql_result = None
        try:
            self.cursor.execute(query_sql, query_dict)
            sql_result = self.cursor.fetchall()
            return True, sql_result
        except Exception, err:
            print err
            return False, sql_result


    def insert(self, tablename, data_dict):
        """
            insert single line data to table, do not forget to use commit() function

            Args:
                    tablename   表名
                    data_dict   数据字典

            Returns:
                    True or False
        """
        # form insert sql
        key_string, value_string = '', ''
		# alter by huang on 2015-09-14 for 将  iteritems() 替换成 iterkeys()
        #for key_item, value_item in data_dict.iteritems():
        for key_item in data_dict.iterkeys():
            key_string += '%s,' % key_item
            value_string += "%%(%s)s" % key_item + ','
        insert_sql = """INSERT INTO %s (%s) VALUES (%s);""" % (tablename, key_string[:-1], value_string[:-1])

        # excute insert sql
        try:
            self.cursor.execute(insert_sql, data_dict)
            return True
        except Exception, err:
            print err
            return False

    def update(self, update_sql, update_dict):
        """
            update db
        """
        try:
            self.cursor.execute(update_sql, update_dict)
            return True
        except Exception, err:
            print err
            return False


    # del by huang on 2015-08-31 for nolonger use
    #def delete(self, delete_sql, delete_dict):
    #    """
    #        update db
    #    """
    #    try:
    #        self.cursor.execute(delete_sql, delete_dict)
    #        return True
    #    except Exception, err:
    #        print err
    #        return False


    def commit(self):
        """
            commit transaction
        """
        try:
            self.conn.commit()
            return True
        except Exception, err:
            print err
            return False


    def close(self):
        """
            close connect
        """
        self.conn.close()


if __name__ == '__main__':
    db_test = PostgresClient(host=conf.pg_host,
                                port=conf.pg_port,
                                user=conf.pg_user,
                                password=conf.pg_password,
                                database=conf.pg_database
                            )
