#!/usr/bin/python
#! -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'root', 'Team3', 'NFL_Predictions');

with con:

	cur = con.cursor()
	cur.execute("SET sql_notes = 0;")
	cur.execute("DROP TABLE IF EXISTS tblTeam")
	cur.execute("CREATE TABLE IF NOT EXISTS tblTeam(TeamID INT AUTO_INCREMENT NOT NULL, TeamNameFull VARCHAR(30), TeamNameAbbr VARCHAR(4), TeamOrigin VARCHAR(50), TeamRank INT, CONSTRAINT tblTeam_pk PRIMARY KEY (TeamID, TeamNameAbbr, TeamRank))")
