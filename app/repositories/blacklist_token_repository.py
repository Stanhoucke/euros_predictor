from db.run_sql import run_sql
from models.blacklist import Blacklist

def save(blacklist_token):
    sql = "INSERT INTO blacklist_tokens (token, blacklist_date) VALUES (%s, %s) RETURNING id"
    values = [blacklist_token.token, blacklist_token.blacklist_date]
    result = run_sql(sql, values)
    blacklist_token.id = result[0]['id']
    return blacklist_token

def check_blacklist(auth_token):
    sql = "SELECT * FROM blacklist_tokens WHERE token = %s"
    values = [auth_token]
    result = run_sql(sql, values)

    if len(result) > 0:
        return True
    else: 
        return False
