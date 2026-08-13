from configuration.db_configuration import db
from model import AbstractUser
from model.enums import AgentType

class Agent(AbstractUser):
    __tablename__ = 'agents'

    user_type = 'agent'

    agent_type = db.Column(db.Enum(AgentType), nullable=False)
    establishment_id = db.Column(db.Integer, db.ForeignKey('establishments.id'), nullable=False)

    establishment = db.relationship('Establishment', lazy='joined')

    def __init__(self, name: str, email: str, password: str, agent_type: AgentType, establishment_id: int) -> None:
        super().__init__(name, email, password)
        self.agent_type = agent_type
        self.establishment_id = establishment_id

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update({
            'agent_type': self.agent_type,
            'establishment': self.establishment.to_dict() if self.establishment else None
        })
        return data