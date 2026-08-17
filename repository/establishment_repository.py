from configuration.db_configuration import db
from model import Establishment

class EstablishmentRepository:
    def create(self, establishment: Establishment) -> Establishment:
        db.session.add(establishment)
        db.session.commit()
        return establishment

    def get(self, establishment_id: int) -> Establishment | None:
        return db.session.get(Establishment, establishment_id)

    def update(self, establishment_id: int, data: Establishment) -> Establishment | None:
        establishment = db.session.get(Establishment, establishment_id)
        data.id = establishment_id
        establishment = data
        db.session.commit()
        return establishment

    def delete(self, establishment_id: int) -> bool:
        establishment = db.session.get(establishment_id)
        if not establishment:
            return False
        db.session.delete(establishment)
        db.session.commit()
        return True
    
