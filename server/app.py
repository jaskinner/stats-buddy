from flask import Flask

from gameStats import GameStats
from teams import nba_teams
from teamStats import TeamStats
from playerStats import PlayerStats
from players import nba_players

from translator import Translator

app = Flask(__name__)


@app.route('/')
def hello():
    return 'hello'


@app.route('/player/<player_id>')
def get_player(player_id):
    pass


@app.route('/players')
def get_players():
    return Translator(nba_players).returnJSON()


@app.route('/players/<team_id>')
def get_players_by_team(team_id):
    pass


@app.route('/teams')
def get_teams():
    return nba_teams


@app.route('/stats/<team>/<season>/<stat>')
def get_ytd_team_stat(team, stat, season):
    return TeamStats(team, stat).get_season_stat(season=season)


@app.route('/stats/<player_id>/<range>')
def get_ytd_player_stat(player_id, range):
    return PlayerStats(player_id).get_player_stat()[range]


@app.route('/games/<team_id>')
def get_reb_stats(team_id):
    stats = GameStats(team_id=team_id).get_average_atr()
    return stats


@app.route('/matchup')
def get_matchup_stats():
    return GameStats().get_average_atr()
