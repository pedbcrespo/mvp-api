from model.agent import Agent
from model.request.agent_request import AgentRequest
from repository.user_repository import UserRepository

class AgentRepository(UserRepository):
    def get_by_email(self, email: str) -> Agent | None:
        return super().get_by_email(email, Agent)

    def get(self, agent_id: int) -> Agent | None:
        return super().get(agent_id, Agent)

    def update(self, agent_id: int, data: AgentRequest) -> Agent | None:
        return super().update(agent_id, data, Agent)

    def delete(self, agent_id: int) -> bool:
        return super().delete(agent_id, Agent)

    def create(self, agent: Agent) -> Agent:
        return super().create(agent)