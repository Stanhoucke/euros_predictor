from werkzeug.security import generate_password_hash, check_password_hash
import repositories.blacklist_token_repository as blacklist_token_repository
import datetime
import jwt
import os

class Player():
    def __init__(self, email, password, first_name, last_name, team_name, points=0, id=None):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.team_name = team_name
        self.points = points
        self.id = id

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def hash_password(self):
        self.password = generate_password_hash(self.password)
    
    def check_password(self, check):
        return check_password_hash(self.password, check)

    def encode_jwt(self, player_id):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=0),
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

    @staticmethod
    def decode_jwt(auth_token):
        try:
            payload = jwt.decode(auth_token, os.environ.get('SECRET_KEY'), algorithms='HS256')
            is_blacklisted_token = blacklist_token_repository.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token is blacklisted. Please log in again.'
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError:
            return "Signature expired. Please log in again." 
        except jwt.InvalidTokenError:
            return "Invalid token. Please log in again."       
