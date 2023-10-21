from utils import db


class Vehicle(db.Model):
    __tablename__ = 'tbl_vehicle'

    id = db.Column(db.Integer, primary_key=True)
    license = db.Column(db.String(255), nullable=False)
    driver = db.Column(db.String(255), nullable=False)

    @staticmethod
    def get_all():
        return Vehicle.query.all()

    @staticmethod
    def get_by_id(id):
        return Vehicle.query.get(id)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()