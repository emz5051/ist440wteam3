import nflgame

games = nflgame.games(2015, week=5)
plays = nflgame.combine_plays(games)
for p in plays.sort('passing_yds').limit(7):
	print p
