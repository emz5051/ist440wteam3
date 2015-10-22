#!/usr/bin/python
#! -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'root', 'Team3', 'NFL_Predictions');

with con:

	cur = con.cursor()
	cur.execute("SET sql_notes = 0;")
	cur.execute("DROP TABLE IF EXISTS tblPlayerStats")
	cur.execute("CREATE TABLE IF NOT EXISTS tblPlayerStats(PlayerStatsID INT AUTO_INCREMENT NOT NULL, PlayerID INT NOT NULL, Position VARCHAR(5), Total_Rec INT, Rec_YDS INT, Rec_AVG INT, TDs INT, TCKL INT, FF INT, Interceptions INT, SCKS NUMERIC, Pass_YDS INT, Rush_YDS INT, PlayerRank INT, CONSTRAINT tblPlayerStats_pk PRIMARY KEY (PlayerStatsID), CONSTRAINT tblPlayerStats_fk FOREIGN KEY (PlayerID) REFERENCES tblPlayer (PlayerID))")
