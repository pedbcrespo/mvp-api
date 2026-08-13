from configuration.db_configuration import db
from model import User

class UserRepository:
    def login(self, email: str, password: str) -> User | None:
        user = db.session.query(User).filter_by(email=email, password=password).first()
        return user