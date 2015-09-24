#!/usr/bin/python
#-*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'root', 'Team3', 'TestDB');

with con:

	cur = con.cursor()

	cur.execute("DELETE FROM Test WHERE Id = %s", ("2"))

	print "Number or rows updated:", cur.rowcount
