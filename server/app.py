from flask import Flask
from teams import nba_teams
from teamStats import TeamStats

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
    pass


@app.route('/players/<team_id>')
def get_players_by_team(team_id):
    pass


@app.route('/teams')
def get_teams():
    return Translator(nba_teams).returnJSON()


@app.route('/stats/<team>/<season>/<stat>')
def get_ytd_team_stat(team, stat, season):
    return TeamStats(team, stat).get_season_stat(season=season)


@app.route('/games')
def get_games():
    pass
