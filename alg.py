import nflgame

games = nflgame.games(2015, week=1)

#Teams Offensive Ranks

teamsPPG = nflgame.combine_game_stats(games)
for t in teamsPPG.PPG().sort('PPG'):
        msg = 'The %s score %d points per game'
        print msg % (t, t.PPG)
		
teamsPassYds = nflgame.combine_game_stats(games)
for t in teamsPassYds.PassYds().sort('PassYds'):
        msg = 'The %s average %d passing yards per game'
        print msg % (t, t.PassYds)

teamsRushYds = nflgame.combine_game_stats(games)
for t in teamsRushYds.RushYds().sort('RushYds'):
        msg = 'The %s average %d rushing yards per game'
        print msg % (t, t.RushYds)
		
teamsTotalYds = nflgame.combine_game_stats(games)
for t in teamsTotalYds.TotalYds().sort('TotalYds'):
        msg = 'The %s average %d total yards per game'
        print msg % (t, t.TotalYds)
		
teamsTO = nflgame.combine_game_stats(games)
for t in teamsTO.TO().sort('TO'):
        msg = 'The %s average %d turnovers per game'
        print msg % (t, t.TO)
		
teamsSacks = nflgame.combine_game_stats(games)
for t in teamsSacks.Sacks().sort('Sacks'):
        msg = 'The %s average %d sacks per game'
        print msg % (t, t.Sacks)
		
teamsRecYdsAtt = nflgame.combine_game_stats(games)
for t in teamsRecYdsAtt.RecYdsAtt().sort('RecYdsAtt'):
        msg = 'The %s average %d receiving yards per attempt'
        print msg % (t, t.RecYdsAtt)
		
teamsRushYdsAtt = nflgame.combine_game_stats(games)
for t in teamsRushYdsAtt.RushYdsAtt().sort('RushYdsAtt'):
        msg = 'The %s average %d rushing yards per attempt'
        print msg % (t, t.RushYdsAtt)
		
		
		
		
#Teams Defensive Ranks

teamsPtsAlw = nflgame.combine_game_stats(games)
for t in teamsPtsAlw.PtsAlw().sort('PtsAlw'):
        msg = 'The %s average %d points allowed per game'
        print msg % (t, t.PtsAlw)
		
teamsPassYdsAlw = nflgame.combine_game_stats(games)
for t in teamsPassYdsAlw.PassYdsAlw().sort('PassYdsAlw'):
        msg = 'The %s average %d passing yards allowed per game'
        print msg % (t, t.PassYdsAlw)

teamsRushYdsAlw = nflgame.combine_game_stats(games)
for t in teamsRushYdsAlw.RushYdsAlw().sort('RushYdsAlw'):
        msg = 'The %s average %d rushing yards allowed per game'
        print msg % (t, t.RushYdsAlw)
		
teamsTotalYdsAlw = nflgame.combine_game_stats(games)
for t in teamsTotalYdsAlw.TotalYdsAlw().sort('TotalYdsAlw'):
        msg = 'The %s average %d total yards allowed per game'
        print msg % (t, t.TotalYdsAlw)
		
teamsFTO = nflgame.combine_game_stats(games)
for t in teamsFTO.FTO().sort('FTO'):
        msg = 'The %s average %d forced turnovers per game'
        print msg % (t, t.FTO)
		
teamsFSacks = nflgame.combine_game_stats(games)
for t in teamsFSacks.FSacks().sort('FSacks'):
        msg = 'The %s average %d forced sacks per game'
        print msg % (t, t.FSacks)
		
teamsFSacks = nflgame.combine_game_stats(games)
for t in teamsFSacks.FSacks().sort('FSacks'):
        msg = 'The %s average %d forced sacks per game'
        print msg % (t, t.FSacks)
		
teamsRecYdsAlwAtt = nflgame.combine_game_stats(games)
for t in teamsRecYdsAlwAtt.RecYdsAlwAtt().sort('RecYdsAlwAtt'):
        msg = 'The %s average %d receiving yards allowed per attempt'
        print msg % (t, t.RecYdsAlwAtt)
		
teamsRushYdsAlwAtt = nflgame.combine_game_stats(games)
for t in teamsRushYdsAlwAtt.RushYdsAlwAtt().sort('RushYdsAlwAtt'):
        msg = 'The %s average %d rushing yards allowed per attempt'
        print msg % (t, t.RushYdsAlwAtt)

		
		
