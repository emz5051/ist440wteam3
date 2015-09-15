#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'root', 'Team3', 'TestDB');

with con:

	cur = con.cursor()
	cur.execute("SELECT * FROM Test")

	rows = cur.fetchall()

	for row in rows:
		print row
