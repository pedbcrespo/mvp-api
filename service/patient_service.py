from repository import PatientRepository
from model.request import PatientRequest
from model import Patient
from datetime import datetime
from service.token_service import TokenService

class PatientService:
    def __init__(self, repository: PatientRepository):
        self.repository = repository
        self.token_service = TokenService()

    def get(self, patient_id: int) -> dict | None:
        patient = self.repository.get(patient_id)
        if patient:
            return patient.to_dict()
        return None

    def login(self, email: str, password: str) -> dict | None:
        patient = self.repository.get_by_email(email)
        if patient and patient.password == password:
            response = patient.to_dict()
            response['token'] = self.token_service.generate_token(patient)
            return response
        return None

    def register(self, patient_request: 'PatientRequest') -> dict:
        patient = self.__generate_patient_by_request(patient_request)
        if not self.__validate_patient(patient):
            raise ValueError("Invalid patient data")
        patient = self.repository.create(patient)
        return patient.to_dict()

    def update(self, token: str, patient_id: int, patient_request: 'PatientRequest') -> dict:
        if not self.token_service.validate_request(token):
            raise ValueError("Invalid token")

        patient = self.repository.get(patient_id)
        if not patient:
            raise ValueError("Invalid patient data")

        patient_to_update = self.__generate_patient_by_request(patient_request)
        patient_to_update.id = patient_id
        patient_to_update.email = patient.email
        patient = self.repository.update(patient_id, patient_to_update)
        return patient.to_dict()

    def delete(self, token: str, patient_email: str) -> dict:
        if not self.token_service.validate_request(token):
            raise ValueError("Invalid token")

        patient = self.repository.get_by_email(patient_email)
        if not patient:
            raise ValueError("Invalid patient data")

        isDeleted = self.repository.delete(patient.id)
        return {'message': 'pacient deleted'} if isDeleted else {'error': 'pacient could not be deleted'}

    def __validate_patient(self, patient: Patient) -> bool:
        if not patient.name or not patient.birth_date or not patient.email or not patient.password or not patient.address:
            return False
        return True

    def __generate_patient_by_request(self, patient_request: PatientRequest) -> Patient:
        birth_date = datetime.strptime(patient_request.birth_date, '%Y-%m-%d').date()
        return Patient(
            name=patient_request.name,
            email=patient_request.email,
            password=patient_request.password,
            birth_date=birth_date,
            address=patient_request.address
        )