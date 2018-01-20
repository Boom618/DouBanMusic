#!/usr/bin/env python3
# encoding:utf-8

import sqlite3


class SQL_Method:
    def creatDB(self):
        connect = sqlite3.connect("Douban.db")
        cursor = connect.cursor()

        # 创建表
        cursor.execute('''CREATE TABLE IF NOT EXISTS DOUBLE 
               (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
               TITLE1          CHAR(50),
               HREF           CHAR(100),
               SCORE        FLOAT ,
               NUM        TEXT ,
               IMG        CHAR(100));''')
        print("Table created successfully")
        connect.commit()

        cursor.close()
        connect.close()

    def insertDB(self, href, title, score, num, img):
        connect = sqlite3.connect("Douban.db")
        cursor = connect.cursor()

        cursor.execute("INSERT INTO DOUBLE (HREF,TITLE1,SCORE,NUM,IMG) "
                       "VALUES ('" + href + " ',' " + title + "','" + score + "','" + num + "','" + img + "')")

        connect.commit()
        print("插入数据成功")

        cursor.close()
        connect.close()
