from configuration import db
from model import AbstractUser

class Patient(AbstractUser):
    __tablename__ = 'patients'

    user_type = 'patient'

    birth_date = db.Column(db.Date, nullable=False)
    address = db.Column(db.String(200), nullable=False)

    def __init__(self, name: str, email: str, password: str, birth_date: str, address: str) -> None:
        super().__init__(name, email, password)
        self.birth_date = birth_date
        self.address = address

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update({
            'birth_date': self.birth_date,
            'address': self.address
        })
        return data