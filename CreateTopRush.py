#!/usr/bin/python
#! -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'root', 'Team3', 'NFL_Test');

with con:

        cur = con.cursor()
        cur.execute("SET sql_notes = 0; ")
        cur.execute("DROP TABLE IF EXISTS TopRush")
        cur.execute("CREATE TABLE IF NOT EXISTS TopRush(ID INT AUTO_INCREMENT NOT NULL, Name VARCHAR(35), Num_Carries INT, Num_Yards INT, Num_TDs INT, CONSTRAINT TopRush_pk PRIMARY KEY (ID))")
