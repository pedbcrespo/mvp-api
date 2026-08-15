from dataclasses import dataclass
from model.request.user_request import UserRequest
from model.enums.agent_type import AgentType


@dataclass
class AgentRequest(UserRequest):
    establishment_id: int
    agent_type: str
    
    @staticmethod
    def from_dict(data: dict) -> 'AgentRequest':
        return AgentRequest(
            name=data.get('name'),
            email=data.get('email'),
            password=data.get('password'),
            agent_type=data.get('agent_type'),
            establishment_id=data.get('establishment_id')
        )