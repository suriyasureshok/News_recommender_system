import jwt
from datetime import datetime, timedelta
from flask import current_app

def generate_token(u_id):
    payload = {'user_id': u_id, 'exp': datetime.utcnow() + timedelta(days=7)}
    return jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')

def verify_token(token):
    try:
        data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        return data['user_id']
    except Exception:
        return None
