from flask import Flask

app = Flask(__name__)

# Import controller blueprints
from controllers.teams_controller import teams_blueprint
from controllers.groups_controller import groups_blueprint
from controllers.player_controller import players_blueprint

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