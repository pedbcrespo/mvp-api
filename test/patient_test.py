from configuration import BASE_URL
from model.request import PatientRequest

def test_register_patient(client):
    patient_request = PatientRequest(
        name="John Doe",
        birth_date="1990-01-01",
        email="john.doe@example.com"
    )
    response = client.post(f"{BASE_URL}/patients", json=patient_request.dict())
    assert response.status_code == 201