#!/usr/bin/python
#! -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'root', 'Team3', 'NFL_Predictions');

with con:
	
	cur = con.cursor()
	cur.execute("SET sql_notes = 0; ")
	cur.execute("DROP TABLE IF EXISTS tblPlayer")
	cur.execute("CREATE TABLE IF NOT EXISTS tblPlayer(PlayerID INT AUTO_INCREMENT NOT NULL, PlayerFN VARCHAR(35), PlayerLN VARCHAR(35), PlayerTeam VARCHAR(5), DOB DATE, Height INT, Weight INT,Position VARCHAR(4),PlayerRank INT, CONSTRAINT tblPlayer_pk PRIMARY KEY (PlayerID, PlayerRank))")
