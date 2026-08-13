from configuration import db

class Diagnosis(db.Model):
    __tablename__ = 'diagnoses'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    agent_id = db.Column(db.Integer, db.ForeignKey('agents.id'), nullable=False)

    agent = db.relationship('Agent', lazy='joined')
    patient = db.relationship('Patient', lazy='joined')

    def __init__(self, agent_id: int, patient_id: int, description: str) -> None:
        self.description = description
        self.agent_id = agent_id
        self.patient_id = patient_id

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'description': self.description,
            'agent': self.agent.to_dict() if self.agent else None,
            'patient': self.patient.to_dict() if self.patient else None
        }