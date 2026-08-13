from repository import PatientRepository
from model.request import PatientRequest

class PatientService:
    def __init__(self, repository: PatientRepository):
        self.repository = repository

    def get(self, patient_id: int) -> dict | None:
        patient = self.repository.get(patient_id)
        if patient:
            return patient.to_dict()
        return None

    def login(self, email: str, password: str) -> dict | None:
        patient = self.repository.get_by_email(email)
        if patient and patient.password == password:
            return patient.to_dict()
        return None

    def register(self, patient_request: 'PatientRequest') -> dict:
        patient = self.repository.create(patient_request)
        if not self.__validate_patient(patient):
            raise ValueError("Invalid patient data")
        return patient.to_dict()

    def __validate_patient(self, patient) -> bool:
        if not patient.name or not patient.birth_date or not patient.email or not patient.password or not patient.address:
            return False
        return True