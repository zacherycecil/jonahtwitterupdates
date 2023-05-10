#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('jtu.db')

conn.execute('DROP TABLE WINNERS;')
conn.execute('DROP TABLE CONTENDERS;')

conn.execute('''CREATE TABLE WINNERS
         (NAME           TEXT    NOT NULL,
         WEEK            TEXT    NOT NULL,
         LIKECOUNT       INT     NOT NULL);''')

conn.execute('''CREATE TABLE CONTENDERS
         (NAME           TEXT    NOT NULL,
         LIKECOUNT       INT     NOT NULL);''')

print("+1")

conn.close()