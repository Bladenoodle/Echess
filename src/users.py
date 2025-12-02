"""Module containing functions for users management"""
from werkzeug.security import check_password_hash, generate_password_hash
from database_files import db

def create_user(username, password):
    """create user with a given username and password"""
    password_hash = generate_password_hash(password)
    sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
    db.execute(sql, [username, password_hash])

def check_login(username, password):
    """check user login validity"""
    sql = "SELECT id, password_hash FROM users WHERE username = ?"
    result = db.query(sql, [username])

    if not result:
        return None

    user = result[0]
    user_id = user["id"]
    password_hash = user["password_hash"]
    if check_password_hash(password_hash, password):
        return user_id
    return None
