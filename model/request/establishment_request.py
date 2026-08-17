from dataclasses import dataclass

@dataclass
class UserRequest:
    name: str
    adress: str
    city: str
    state: str

    @staticmethod
    def from_dict(data: dict) -> 'UserRequest':
        return UserRequest(
            name=data.get('name'),
            address=data.get('address'),
            city=data.get('city'),
            state=data.get('state')
        )