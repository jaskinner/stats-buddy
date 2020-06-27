from nba_api.stats.endpoints import leaguegamefinder


def get_stat_per_game(games, stat):
    return stat/games


class GameStats:
    stats = None

    def __init__(self, team_id):

        self.stats = leaguegamefinder.LeagueGameFinder(team_id_nullable=team_id,
                                                       season_nullable="2019-20",
                                                       date_to_nullable="02/04/2020"
                                                       ).get_normalized_dict()["LeagueGameFinderResults"]
        self.get_average_atr()

    # def get_orpg(self):
    #     self.response['orpg'] = []
    #     for stat in self.stats:
    #         self.response['orpg'].append(stat["OREB"])
    #
    # def get_average_orbg(self):
    #     a_orpg = 0
    #     for stat in self.stats:
    #         a_orpg += stat["OREB"]
    #
    #     self.response["a_orpg"] = a_orpg / len(self.stats)

    def get_atr(self):
        atr = []
        for stat in self.stats:
            if stat["TOV"] == 0:
                ratio = 12345678
            else:
                ratio = stat["AST"]/stat["TOV"]
            atr.insert(0, ([stat["GAME_DATE"], round(ratio, 2)]))

    def get_average_atr(self):
        ast = 0
        tov = 0
        response = {
            "x": 0,
            "y": 0,
            "z": 0,
            "name": self.stats[0]["TEAM_ABBREVIATION"],
            "fullname": self.stats[0]["TEAM_NAME"]
        }
        for stat in self.stats:
            ast += stat["AST"]
            tov += stat["TOV"]

        response["x"] = get_stat_per_game(len(self.stats), ast)
        response["y"] = get_stat_per_game(len(self.stats), tov)
        response["z"] = round(get_stat_per_game(len(self.stats), ast) / get_stat_per_game(len(self.stats), tov), 2)
        return
