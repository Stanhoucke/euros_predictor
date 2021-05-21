from flask import Flask, render_template, flash, jsonify, make_response
import repositories.player_repository as player_repository
import repositories.team_repository as team_repository

# Import controller blueprints
from controllers.teams_controller import teams_blueprint
from controllers.groups_controller import groups_blueprint
from controllers.player_controller import players_blueprint

app = Flask(__name__)
# Secret key for flash messaging
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Register blueprints
app.register_blueprint(players_blueprint, url_prefix="/api")
app.register_blueprint(teams_blueprint, url_prefix="/api")
app.register_blueprint(groups_blueprint, url_prefix="/api")

@app.route('/')
def home():
    return "Euros Predictor API"

if __name__ == '__main__':
    app.run(debug=True)