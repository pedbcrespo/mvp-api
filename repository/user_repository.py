from configuration.db_configuration import db
from model.abstract_user import AbstractUser
from model.request import UserRequest


class UserRepository:
    def get_by_email(self, email: str, user_model: type[AbstractUser]) -> AbstractUser | None:
        return db.session.query(user_model).filter_by(email=email).first()

    def get(self, user_id: int, user_model: type[AbstractUser]) -> AbstractUser | None:
        return db.session.get(user_model, user_id)

    def create(self, user: AbstractUser) -> AbstractUser:
        db.session.add(user)
        db.session.commit()
        return user

    def update(self, user_id: int, data: UserRequest, user_model: type[AbstractUser]) -> type[AbstractUser] | None:
        user = db.session.get(user_model, user_id)
        if not user:
            return None
        for key, value in vars(data).items():
            if key == 'email':
                continue
            setattr(user, key, value)
        db.session.commit()
        return user

    def delete(self, user_id: int,  user_model: type[AbstractUser]) -> bool:
        user = db.session.get(user_model, user_id)
        if not user:
            return False
        db.session.delete(user)
        db.session.commit()
        return True

    