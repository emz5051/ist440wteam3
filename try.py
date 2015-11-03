#!/usr/bin/pytho
#! -*- coding: utf-8 -*-

import nflgame
import MySQLdb as mdb

con = mdb.connect('localhost', 'root', 'Team3', 'NFL_Test');
with con:
	games = nflgame.games(2015, week=7)
	players = nflgame.combine_game_stats(games)
	for p in players.rushing().sort('rushing_yds').limit(10):
		cur = con.cursor()
		cur.execute("INSERT INTO TopRush (Name, Num_Carries, Num_Yards, Num_TDs) VALUES (%s, %d, %d, %d)")
    

