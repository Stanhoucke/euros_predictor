from flask import Flask, render_template, flash

# Import controller blueprints
# from controllers.members_controller import members_blueprint


app = Flask(__name__)
# Secret key for flash messaging
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Register blueprints
# app.register_blueprint(members_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)