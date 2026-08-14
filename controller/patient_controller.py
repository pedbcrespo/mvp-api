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

@patient_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    patient_request = PatientRequest.from_dict(data)
    patient = service.register(patient_request)
    return jsonify(patient), 201

@patient_bp.route('/update/<int:patient_id>', methods=['PUT'])
def update(patient_id: int):
    data = request.get_json()
    token = get_token()
    patient_request = PatientRequest.from_dict(data)
    patient = service.update(token, patient_id, patient_request)
    return jsonify(patient), 201

def get_token():
    auth_header = request.headers.get('Authorization')
    token = auth_header.split(' ')[1]
    return token