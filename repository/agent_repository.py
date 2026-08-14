from configuration import db
from model import Agent
from model.request import AgentRequest

class AgentRepository:
    def create(self, agent: Agent) -> Agent | None:
        db.session.add(agent)
        db.session.commit()
        return agent

    def get(self, agent_id: int) -> Agent | None:
        agent = db.session.get(Agent, agent_id)
        return agent

    def get_by_email(self, email: str) -> Agent | None:
        agent = db.session.query(Agent).filter_by(email=email).first()
        return agent

    def update(self, agent_id: int, data: AgentRequest) -> Agent | None:
        agent = db.session.get(Agent, agent_id)
        if not agent:
            return None
        agent.name = data.name
        agent.establishment_id = data.establishment_id
        agent.password = data.password
        db.session.commit()
        return agent

    def delete(self, agent_id: int) -> bool:
        agent = db.session.get(Agent, agent_id)
        if not agent:
            return False
        db.session.delete(agent)
        db.session.commit()
        return True