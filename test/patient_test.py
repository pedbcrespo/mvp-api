from configuration.const_configuration import BASE_URL
from model.request import PatientRequest


def test_register_patient(client):
    patient_request = PatientRequest(
        name="John Doe",
        email="john.doe@example.com",
        password="securepassword",
        birth_date="1990-01-01",
        address="Rua das Flores, 123, São Paulo, SP, Brasil"
    )
    response = client.post(f"{BASE_URL}/patients/register", json=patient_request)
    assert response.status_code == 201