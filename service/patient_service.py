from repository import PatientRepository
from model.request import PatientRequest
from model import Patient
from datetime import datetime
from service.token_service import TokenService
from service.user_service import UserService
from typing import override

class PatientService(UserService):
    def __init__(self, repository: PatientRepository):
        super().__init__(repository)

    @override
    def update(self, token: str, patient_request: PatientRequest) -> dict:
        patient_request.birth_date = datetime.strptime(patient_request.birth_date, '%Y-%m-%d')
        return super().update(token, patient_request)

    def _generate_user_by_request(self, user_request: PatientRequest) -> Patient:
            return Patient(
                name=user_request.name,
                email=user_request.email,
                password=user_request.password,
                birth_date=datetime.strptime(user_request.birth_date, '%Y-%m-%d'),
                address=user_request.address
            )
    
    def _validate_user(self, user: Patient) -> bool:
        return bool(user.name and user.email and user.password and user.birth_date and user.address)