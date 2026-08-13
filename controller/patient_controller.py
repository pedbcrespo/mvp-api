from flask import Blueprint, request, jsonify
from configuration import db, BASE_URL
from model.request import PatientRequest
from service.patient_service import PatientService
from repository.patient_repository import PatientRepository

service = PatientService(PatientRepository())


patient_bp = Blueprint('patient', __name__, url_prefix=f'/{BASE_URL}/patients')


@patient_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    patient = service.login(email, password)
    if not patient:
        return jsonify({'error': 'Patient not found'}), 404
    return jsonify(patient), 200