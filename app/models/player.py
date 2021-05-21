from werkzeug.security import check_password_hash, generate_password_hash
import datetime
import jwt
import os

class Player():
    def __init__(self, email, password, first_name, last_name, team_name, points=0, id=None):
        self.email = email
        self.password = generate_password_hash(password)
        self.first_name = first_name
        self.last_name = last_name
        self.team_name = team_name
        self.points = points
        self.id = id

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def encode_jwt(self, player_id):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=600),
                'iat': datetime.datetime.utcnow(),
                'sub': player_id
            }
            return jwt.encode(
                payload,
                os.environ.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e

    def decode_jwt(self, auth_token):
        try:
            payload = jwt.decode(auth_token, os.environ.get('SECRET_KEY'), algorithms='HS256')
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return "Signature expired. Please log in again." 
        except jwt.InvalidTokenError:
            return "Invalid token. Please log in again."       
