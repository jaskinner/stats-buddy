from nba_api.stats.endpoints import leaguegamefinder


class TeamStats:
    team = None
    stat = None

    def __init__(self, team, stat):
        self.team = team
        self.stat = stat

    def get_season_stat(self, season):
        pass
        # gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=self.team)
        # games = gamefinder.get_dict()
        # games = games[games.SEASON_ID.str[-4:] == '2017']
        # return games

