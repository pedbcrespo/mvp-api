from flask import Blueprint, request, jsonify
from configuration import db, BASE_URL
from service.establishment_service import EstablishmentService
from repository.establishment_repository import EstablishmentRepository

service = EstablishmentService(EstablishmentRepository())

establishment_bp = Blueprint('establishment', __name__, url_prefix=f'/{BASE_URL}/establishments')

@establishment_bp.route('/register', methods=['POST'])
def register():
    pass

@establishment_bp.route('/update', methods=['PUT'])
def update():
    pass

@establishment_bp.route('/delete', methods=['DELETE'])
def delete():
    pass