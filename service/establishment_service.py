from repository import EstablishmentRepository
from model import Establishment
from model.request import EstablishmentRequest

class EstablishmentService:
    def __init__(self, repository: EstablishmentRepository):
        self.repository = repository

    def create(self, establishment: EstablishmentRequest) -> dict:
        if not self._validate_establishment(establishment):
            raise ValueError("Invalid establishment data")
        establishment = self._generate_establishment_by_request(establishment)
        return self.repository.create(establishment).to_dict()

    def get(self, establishment_id: int) -> dict | None:
        establishment = self.repository.get(establishment_id)
        if not establishment:
            return None
        return establishment.to_dict()

    def update(self, establishment_id: int, establishment: EstablishmentRequest) -> dict | None:
        found_establishment = self.repository.get(establishment_id)
        if not found_establishment:
            return None
        return self.repository.update(establishment_id, establishment).to_dict()

    def delete(self, establishment_id: int) -> bool:
        return self.repository.delete(establishment_id)

    def _validate_establishment(self, establishment: EstablishmentRequest) -> bool:
        return bool(establishment.name and establishment.address and establishment.city and establishment.state)

    def _generate_establishment_by_request(self, establishment_request: EstablishmentRequest) -> Establishment:
        return Establishment(
            name=establishment_request.name,
            address=establishment_request.address,
            city=establishment_request.city,
            state=establishment_request.state
        )

    