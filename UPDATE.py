#!/usr/bin/python
#-*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'root', 'Team3', 'TestDB');

with con:

        cur = con.cursor()

        cur.execute("UPDATE Test SET FirstName = %s WHERE Id = %s", ("Mike", "1"))

        print "Number or rows updated:", cur.rowcount

