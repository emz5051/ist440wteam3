#!/usr/bin/python
#! -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'root', 'Team3', 'NFL_Predictions');

with con:

        cur = con.cursor()
        cur.execute("SET sql_notes = 0; ")
        cur.execute("DROP TABLE IF EXISTS tblPlayer")
        cur.execute("CREATE TABLE IF NOT EXISTS tblPlayer(PlayerID INT AUTO_INCREMENT NOT NULL, PlayerFN VARCHAR(35), PlayerLN VARCHAR(35), PlayerTeam VARCHAR(5), DOB DATE, Height INT, Weight INT,Position VARCHAR(4),PlayerRank INT, CONSTRAINT tblPlayer_pk PRIMARY KEY (PlayerID, PlayerRank))")
	cur.execute("DROP TABLE IF EXISTS tblPlayerStats")
        cur.execute("CREATE TABLE IF NOT EXISTS tblPlayerStats(PlayerStatsID INT AUTO_INCREMENT NOT NULL, PlayerID INT NOT NULL, Position VARCHAR(5), Total_Rec INT, Rec_YDS INT, Rec_AVG INT, TDs INT, TCKL INT, FF INT, Interceptions INT, SCKS NUMERIC, Pass_YDS INT, Rush_YDS INT, PlayerRank INT, CONSTRAINT tblPlayerStats_pk PRIMARY KEY (PlayerStatsID), CONSTRAINT tblPlayerStats_fk FOREIGN KEY (PlayerID) REFERENCES tblPlayer (PlayerID))")
	cur.execute("DROP TABLE IF EXISTS tblTeam")
        cur.execute("CREATE TABLE IF NOT EXISTS tblTeam(TeamID INT AUTO_INCREMENT NOT NULL, TeamNameFull VARCHAR(30), TeamNameAbbr VARCHAR(4), TeamOrigin VARCHAR(50), TeamRank INT, CONSTRAINT tblTeam_pk PRIMARY KEY (TeamID, TeamNameAbbr, TeamRank))")
	cur.execute("DROP TABLE IF EXISTS tblTeamStats")
        cur.execute("CREATE TABLE IF NOT EXISTS tblTeamStats (TeamID INT NOT NULL, TeamRank INT, Pass_YPG NUMERIC, Rush_YPG NUMERIC, Total_YPG NUMERIC, Total_PPG NUMERIC, FF INT, Rec_Fum INT, Tackles INT, SCKS NUMERIC, Interceptions INT, INT_TDS INT, CONSTRAINT tblTeamStats_fk FOREIGN KEY (TeamID) REFERENCES tblTeam (TeamID))")
	cur.execute("DROP TABLE IF EXISTS tblRoster")
        cur.execute("CREATE TABLE IF NOT EXISTS tblRoster (PlayerID INT, PlayerFN VARCHAR(35), PlayerLN VARCHAR(35), PlayerRank INT, TeamID INT, TeamNameAbbr VARCHAR(50), Position VARCHAR(4), TeamRank INT, CONSTRAINT tblRoster_fk FOREIGN KEY (PlayerID) REFERENCES tblPlayer (PlayerID), CONSTRAINT fk_tblRoster FOREIGN KEY (TeamID, TeamNameAbbr, TeamRank) REFERENCES tblTeam (TeamID, TeamNameAbbr, TeamRank))")
