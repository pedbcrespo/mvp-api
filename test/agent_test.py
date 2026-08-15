from configuration.const_configuration import BASE_URL
from configuration.db_configuration import db
from model.request import AgentRequest
from model import Agent, Establishment
from model.enums.agent_type import AgentType
from datetime import datetime

def test_register_agent(client, app):
    ESTABLISHMENT_ID_TEST = 1
    with app.app_context():
        establishment = Establishment(
            name="Clinica Teste",
            address="Rua das Flores, 123, São Paulo, SP, Brasil",
            city="São Paulo",
            state="SP"
        )
        establishment.id = ESTABLISHMENT_ID_TEST
        db.session.add_all([establishment])
        db.session.commit()

    agent_request = AgentRequest(
        name="John Doe",
        email="john.doe@example.com",
        password="securepassword",
        establishment_id=ESTABLISHMENT_ID_TEST,
        agent_type=AgentType.DOCTOR.value
    )
    response = client.post(f"{BASE_URL}/agents/register", json=agent_request)
    assert response.status_code == 201

def test_login_agent(client, app):
    EMAIL_TEST = "john.doe@example.com"
    PASSWORD_TEST = "securepassword"
    ESTABLISHMENT_ID_TEST = 1
    with app.app_context():
        establishment = Establishment(
            name="Clinica Teste",
            address="Rua das Flores, 123, São Paulo, SP, Brasil",
            city="São Paulo",
            state="SP"
        )
        establishment.id = ESTABLISHMENT_ID_TEST
        db.session.add_all([establishment])
        db.session.commit()

        registered_agent = Agent(
            name="John Doe",
            email=EMAIL_TEST,
            password=PASSWORD_TEST,
            establishment_id=1,
            agent_type=AgentType.DOCTOR
        )
        db.session.add_all([registered_agent])
        db.session.commit()

    login_data = {
        "email": EMAIL_TEST,
        "password": PASSWORD_TEST
    }

    response = client.post(f"{BASE_URL}/agents/login", json=login_data)
    assert response.status_code == 200
    assert "token" in response.get_json()

def test_update_agent(client, app):
    EMAIL_TEST = "john.doe@example.com"
    PASSWORD_TEST = "securepassword"
    ESTABLISHMENT_ID_TEST = 1
    with app.app_context():
        establishment = Establishment(
            name="Clinica Teste",
            address="Rua das Flores, 123, São Paulo, SP, Brasil",
            city="São Paulo",
            state="SP"
        )
        establishment.id = ESTABLISHMENT_ID_TEST
        db.session.add_all([establishment])
        db.session.commit()

        registered_agent = Agent(
            name="John Doe",
            email=EMAIL_TEST,
            password=PASSWORD_TEST,
            establishment_id=1,
            agent_type=AgentType.DOCTOR
        )
        db.session.add_all([registered_agent])
        db.session.commit()
    login_data = {"email": EMAIL_TEST,"password": PASSWORD_TEST}
    response = client.post(f"{BASE_URL}/agents/login", json=login_data)