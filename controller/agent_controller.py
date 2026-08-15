from flask import Blueprint, request, jsonify
from configuration import db, BASE_URL
from model.request import AgentRequest
from service.agent_service import AgentService
from repository.agent_repository import AgentRepository

service = AgentService(AgentRepository())


agent_bp = Blueprint('agent', __name__, url_prefix=f'/{BASE_URL}/agents')

@agent_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    agent = service.login(email, password)
    if not agent:
        return jsonify({'error': 'Agent not found'}), 404
    return jsonify(agent), 200

@agent_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    agent_request = AgentRequest.from_dict(data)
    agent = service.register(agent_request)
    return jsonify(agent), 201

@agent_bp.route('/update/<int:agent_id>', methods=['PUT'])
def update(agent_id: int):
    data = request.get_json()
    token = get_token()
    agent_request = AgentRequest.from_dict(data)
    agent = service.update(token, agent_id, agent_request)
    return jsonify(agent), 201

@agent_bp.route('/delete/<email>', methods=['DELETE'])
def delete(email: str):
    token = get_token()
    dict = service.delete(token, email)
    status_code = 500 if 'error' in dict else 201
    return jsonify(dict), status_code

def get_token():
    auth_header = request.headers.get('Authorization')
    token = auth_header.split(' ')[1]
    return token