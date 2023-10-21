from utils import db


class School(db.Model):
    __tablename__ = 'tbl_school'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    @staticmethod
    def get_all():
        return School.query.all()

    @staticmethod
    def get_by_id(id):
        return School.query.get(id)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()