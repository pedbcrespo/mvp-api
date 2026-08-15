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

def test_update_patient(client, app):
    EMAIL_TEST = "john.doe@example.com"
    PASSWORD_TEST = "securepassword"
    ID_TEST = 1
    with app.app_context():
        registered_patient = Patient(
            name="John Doe",
            email=EMAIL_TEST,
            password=PASSWORD_TEST,
            birth_date=datetime.strptime('1990-01-01', '%Y-%m-%d').date(),
            address="Rua das Flores, 123, São Paulo, SP, Brasil"
        )
        registered_patient.id = ID_TEST
        db.session.add_all([registered_patient])
        db.session.commit()

    login_data = {"email": EMAIL_TEST,"password": PASSWORD_TEST}
    
    response = client.post(f"{BASE_URL}/patients/login", json=login_data)
    token = response.get_json()['token']
    NEW_PASSWORD_TEST = "newpasswordtest"
    NEW_NAME_TEST = "John Doe Dee"
    patient_to_update = PatientRequest(
        name=NEW_NAME_TEST,
        email="john.doe-dee@example.com",
        password=NEW_PASSWORD_TEST,
        birth_date='1991-02-02',
        address="Rua Siqueira Campos, 123, Rio de Janeiro, RJ, Brasil"
    )
    response = client.put(f"{BASE_URL}/patients/update/", json=patient_to_update, headers={"Authorization": f"Bearer {token}"})
    response_json = response.get_json()
    assert response.status_code == 201
    assert response_json['email'] == EMAIL_TEST
    assert response_json['name'] == NEW_NAME_TEST

def test_delete_patient(client, app):
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

    login_data = { "email": EMAIL_TEST, "password": PASSWORD_TEST }
        
    response = client.post(f"{BASE_URL}/patients/login", json=login_data)
    token = response.get_json()['token']
    response = client.delete(f"{BASE_URL}/patients/delete/", headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 201
    assert 'error' not in response.get_json() 
