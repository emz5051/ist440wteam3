import nflgame


print ('Rushing attempts, rushing yards, rushing touchdowns')
games = nflgame.games(2015, week=6)
players = nflgame.combine(games)
for p in players.rushing().sort("rushing_yds").limit(10):
	print p, p.rushing_att, p.rushing_yds, p.rushing_tds


plays = nflgame.combine_plays(games)
for p in plays.sort('passing_yds').limit(5):
    print p
