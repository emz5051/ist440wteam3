import nflgame

games = nflgame.games(year=2014)
players = nflgame.combine_game_stats(games)
for player in players:
    print player, player.formatted_stats()
