from configuration import db
from model import Patient
from model.request import PatientRequest
from repository.user_repository import UserRepository

class PatientRepository(UserRepository):
    def create(self, patient: Patient) -> Patient | None:
        return super().create(patient)

    def get(self, patient_id: int) -> Patient | None:
        return super().get(patient_id, Patient)

    def get_by_email(self, email: str) -> Patient | None:
        return super().get_by_email(email, Patient)

    def update(self, patient_id: int, data: PatientRequest) -> Patient | None:
        return super().update(patient_id, data, Patient)

    def delete(self, patient_id: int) -> bool:
        return super().delete(patient_id, Patient)