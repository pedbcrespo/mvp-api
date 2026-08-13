from dataclasses import dataclass

from model.request.user_request import UserRequest

@dataclass
class PatientRequest(UserRequest):
    name: str
    birth_date: str
    address: str

    @staticmethod
    def from_dict(data: dict) -> 'PatientRequest':
        return PatientRequest(
            name=data.get('name'),
            birth_date=data.get('birth_date'),
            email=data.get('email'),
            password=data.get('password'),
            address=data.get('address')
        )