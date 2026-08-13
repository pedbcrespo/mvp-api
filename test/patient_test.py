from configuration.const_configuration import BASE_URL
from configuration.db_configuration import db
from model.request import PatientRequest
from model import Patient
from datetime import datetime

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


def test_login_patient(client, app):
    EMAIL_TEST = "john.doe@example.com"
    PASSWORD_TEST = "securepassword"
    with app.app_context():
        registered_patient = Patient(
            name="John Doe",
            email=EMAIL_TEST,
            password=PASSWORD_TEST,
            birth_date=datetime.strptime('1990-01-01', '%Y-%m-%d').date(),
            address="Rua das Flores, 123, São Paulo, SP, Brasil"
        )
        registered_patient.id = 1
        db.session.add_all([registered_patient])
        db.session.commit()

    login_data = {
        "email": EMAIL_TEST,
        "password": PASSWORD_TEST
    }

    response = client.post(f"{BASE_URL}/patients/login", json=login_data)
    assert response.status_code == 200
    assert "token" in response.get_json()