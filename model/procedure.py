from datetime import datetime

from configuration import db
from model.enums.procedure_type import ProcedureType
from model.enums.procedure_status import ProcedureStatus


class Procedure(db.Model):
    __tablename__ = 'procedures'

    id = db.Column(db.Integer, primary_key=True)
    diagnosis_id = db.Column(db.Integer, db.ForeignKey('diagnoses.id'), nullable=False)
    procedure_type = db.Column(db.Enum(ProcedureType), nullable=False)
    frequency = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Enum(ProcedureStatus), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    diagnosis = db.relationship('Diagnosis', lazy='joined')

    def __init__(self, diagnosis_id: int, procedure_type: ProcedureType, frequency: int) -> None:
        self.diagnosis_id = diagnosis_id
        self.procedure_type = procedure_type
        self.frequency = frequency
        self.status = ProcedureStatus.ACTIVE
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'diagnosis': self.diagnosis.to_dict() if self.diagnosis else None,
            'procedure_type': self.procedure_type.value,
            'frequency': self.frequency,
            'status': self.status.value,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }