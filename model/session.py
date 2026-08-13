from configuration.db_configuration import db
from model.enums import ProcedureType, Status
from datetime import datetime

from model.enums.session_status import SessionStatus

class Session(db.Model):
    __tablename__ = 'sessions'

    id = db.Column(db.Integer, primary_key=True)
    procedure_id = db.Column(db.Integer, db.ForeignKey('procedures.id'), nullable=False)
    establishment_id = db.Column(db.Integer, db.ForeignKey('establishments.id'), nullable=False)
    agent_id = db.Column(db.Integer, db.ForeignKey('agents.id'), nullable=False)
    scheduled_date = db.Column(db.DateTime, nullable=False)
    date_performed = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.Enum(SessionStatus), nullable=False)
    observations = db.Column(db.Text, nullable=True)

    procedure = db.relationship('Procedure', lazy='joined')
    establishment = db.relationship('Establishment', lazy='joined')
    agent = db.relationship('Agent', lazy='joined')


    def __init__(self, procedure_id: int, establishment_id: int, agent_id: int, scheduled_date: datetime) -> None:
        self.procedure_id = procedure_id
        self.establishment_id = establishment_id
        self.agent_id = agent_id
        self.scheduled_date = scheduled_date
        self.status = SessionStatus.SCHEDULED

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'procedure': self.procedure.to_dict() if self.procedure else None,
            'establishment': self.establishment.to_dict() if self.establishment else None,
            'agent': self.agent.to_dict() if self.agent else None,
            'scheduled_date': self.scheduled_date,
            'date_performed': self.date_performed,
            'status': self.status.value,
            'observations': self.observations
        }