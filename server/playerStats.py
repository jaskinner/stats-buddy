from nba_api.stats.endpoints import playerdashboardbylastngames


class PlayerStats:
    player_id = ''

    def __init__(self, player_id):
        self.player_id = player_id

    def get_player_stat(self):
        stats = playerdashboardbylastngames.PlayerDashboardByLastNGames(
            player_id=self.player_id,
            season="2019-20",
            date_to_nullable="03/09/2020"
        )

        return {
            "last5": stats.last5_player_dashboard.get_json(),
            "last10": stats.last10_player_dashboard.get_json(),
            "last15": stats.last15_player_dashboard.get_json(),
            "last20": stats.last20_player_dashboard.get_json(),
        }
