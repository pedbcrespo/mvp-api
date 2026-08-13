from dataclasses import dataclass

@dataclass
class UserRequest:
    name: str
    email: str
    password: str

    @staticmethod
    def from_dict(data: dict) -> 'UserRequest':
        return UserRequest(
            name=data.get('name'),
            email=data.get('email'),
            password=data.get('password')
        )