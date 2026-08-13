from configuration import db
from model import Patient
from model.request import PatientRequest

class PatientRepository:
    def create(self, patient: Patient) -> Patient | None:
        db.session.add(patient)
        db.session.commit()
        return patient

    def get(self, patient_id: int) -> Patient | None:
        patient = db.session.get(Patient, patient_id)
        return patient

    def get_by_email(self, email: str) -> Patient | None:
        patient = db.session.query(Patient).filter_by(email=email).first()
        return patient


    def update(self, patient_id: int, data: PatientRequest) -> Patient | None:
        patient = db.session.get(Patient, patient_id)
        if not patient:
            return None
        patient.name = data.name
        patient.birth_date = data.birth_date
        patient.email = data.email
        patient.password = data.password
        patient.address = data.address
        db.session.commit()
        return patient

    def delete(self, patient_id: int) -> bool:
        patient = db.session.get(Patient, patient_id)
        if not patient:
            return False
        db.session.delete(patient)
        db.session.commit()
        return True