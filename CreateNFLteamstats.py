#!/usr/bin/python
#! -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'root', 'Team3', 'NFL_Predictions');

with con:

	cur = con.cursor()
	cur.execute("SET sql_notes = 0;")
	cur.execute("DROP TABLE IF EXISTS tblTeamStats")
	cur.execute("CREATE TABLE IF NOT EXISTS tblTeamStats (TeamID INT NOT NULL, TeamRank INT, Pass_YPG NUMERIC, Rush_YPG NUMERIC, Total_YPG NUMERIC, Total_PPG NUMERIC, FF INT, Rec_Fum INT, Tackles INT, SCKS NUMERIC, Interceptions INT, INT_TDS INT, CONSTRAINT tblTeamStats_fk FOREIGN KEY (TeamID) REFERENCES tblTeam (TeamID))")
