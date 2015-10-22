import nflgame

games = nflgame.games(2015, week=4)
plays = nflgame.combine_plays(games)
for p in plays.sort('rushing_yds').limit(10):
	print p
