from dataclasses import dataclass
from model.request.user_request import UserRequest

@dataclass
class AgentRequest(UserRequest):
    establishment_id: int

    @staticmethod
    def from_dict(data: dict) -> 'AgentRequest':
        return AgentRequest(
            name=data.get('name'),
            email=data.get('email'),
            password=data.get('password'),
            establishment_id=data.get('establishment_id')
        )