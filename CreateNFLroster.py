#!/usr/bin/python
#! -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'root', 'Team3', 'NFL_Predictions');

with con:

	cur = con.cursor()
	cur.execute("SET sql_notes = 0;")
	cur.execute("DROP TABLE IF EXISTS tblRoster")
	cur.execute("CREATE TABLE IF NOT EXISTS tblRoster (PlayerID INT, PlayerFN VARCHAR(35), PlayerLN VARCHAR(35), PlayerRank INT, TeamID INT, TeamNameAbbr VARCHAR(50), Position VARCHAR(4), TeamRank INT, CONSTRAINT tblRoster_fk FOREIGN KEY (PlayerID) REFERENCES tblPlayer (PlayerID), CONSTRAINT fk_tblRoster FOREIGN KEY (TeamID, TeamNameAbbr, TeamRank) REFERENCES tblTeam (TeamID, TeamNameAbbr, TeamRank))")
