import jwt
from datetime import datetime, timedelta, timezone
from model import AbstractUser
from configuration import SECRET_KEY


class TokenService:
    @staticmethod
    def generate_token(user: AbstractUser) -> str:
        payload = {
            'id': user.id,
            'email': user.email,
            'exp': datetime.now(timezone.utc) + timedelta(hours=8)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return token

    @staticmethod
    def decode_token(token: str) -> dict:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            return {'error': 'Token has expired'}
        except jwt.InvalidTokenError:
            return {'error': 'Invalid token'}
        except Exception as e:
            return {'error': str(e)}

    @staticmethod
    def validate_request(token: str) -> bool:
        payload = TokenService.decode_token(token)
        return 'error' not in payload