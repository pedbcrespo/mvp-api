from model.abstract_user import AbstractUser
from model.request import UserRequest
from repository.user_repository import UserRepository
from service.token_service import TokenService


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository
        self.token_service = TokenService()

    def login(self, email: str, password: str):
        user = self.repository.get_by_email(email)
        if user and user.password == password:
            response = user.to_dict()
            response['token'] = self.token_service.generate_token(user)
            return response
        return None

    def get(self, user_id: int) -> dict | None:
        user = self.repository.get(user_id)
        if user:
            return user.to_dict()
        return None

    def register(self, user_request: UserRequest) -> dict:
        user = self._generate_user_by_request(user_request)
        if not self._validate_user(user):
            raise ValueError("Invalid user data")
        user = self.repository.create(user)
        return user.to_dict()

    def update(self, token: str, user_id: int, user_request: UserRequest) -> dict:
        if not self.token_service.validate_request(token):
            raise ValueError("Invalid token")

        user = self.repository.get(user_id)
        if not user:
            raise ValueError("Invalid user data")

        user = self.repository.update(user_id, user_request)
        return user.to_dict()

    def delete(self, token: str, email: str) -> dict:
        if not self.token_service.validate_request(token):
            raise ValueError("Invalid token")

        user = self.repository.get_by_email(email)
        if not user:
            raise ValueError("Invalid user data")

        is_deleted = self.repository.delete(user.id)
        return {'message': 'user deleted'} if is_deleted else {'error': 'user could not be deleted'}

    def _generate_user_by_request(self, user_request: UserRequest) -> AbstractUser:
        raise NotImplementedError("Subclasses should implement _generate_user_by_request")

    def _validate_user(self, user: AbstractUser) -> bool:
        raise NotImplementedError("Subclasses should implement _validate_user")