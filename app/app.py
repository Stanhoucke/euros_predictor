from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app)

# Import controller blueprints
from controllers.teams_controller import teams_blueprint
from controllers.player_teams_controller import player_teams_blueprint
from controllers.player_controller import player_blueprint
from controllers.groups_controller import groups_blueprint
from controllers.prediction_controller import prediction_blueprint
from controllers.auth_controller import auth_blueprint

# Secret key for flash messaging
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Register blueprints
app.register_blueprint(auth_blueprint, url_prefix="/api")
app.register_blueprint(teams_blueprint, url_prefix="/api")
app.register_blueprint(player_teams_blueprint, url_prefix="/api")
app.register_blueprint(player_blueprint, url_prefix="/api")
app.register_blueprint(groups_blueprint, url_prefix="/api")
app.register_blueprint(prediction_blueprint, url_prefix="/api")

@app.route('/')
def home():
    return "Euros Predictor API"

if __name__ == '__main__':
    app.run(debug=True)