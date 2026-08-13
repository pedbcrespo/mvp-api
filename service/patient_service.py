from repository import PatientRepository

class PatientService:
    def __init__(self, repository: PatientRepository):
        self.repository = repository

    def login(self, email: str, password: str) -> dict | None:
        patient = self.repository.get_by_email(email)
        if patient and patient.password == password:
            return patient.to_dict()
        return None