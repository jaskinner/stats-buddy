from nba_api.stats.static import players

# get_teams returns a list of 30 dictionaries, each an NBA team.
nba_players = players.get_players()


class Players:
    def __init__(self):
        pass
