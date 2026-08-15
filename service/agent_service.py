from model.agent import Agent
from model.request.agent_request import AgentRequest
from model.enums.agent_type import AgentType
from repository.agent_repository import AgentRepository
from service.user_service import UserService


class AgentService(UserService):
    def __init__(self, repository: AgentRepository):
        super().__init__(repository)

    def _generate_user_by_request(self, user_request: AgentRequest) -> Agent:
        return Agent(
            name=user_request.name,
            email=user_request.email,
            password=user_request.password,
            agent_type=AgentType(user_request.agent_type),
            establishment_id=user_request.establishment_id
        )

    def _validate_user(self, user: Agent) -> bool:
        return bool(user.name and user.email and user.establishment_id)