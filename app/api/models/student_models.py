from utils import db


class Student(db.Model):
    __tablename__ = 'tbl_student'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    photo = db.Column(db.Text, nullable=False)

    @staticmethod
    def get_all():
        return Student.query.all()

    @staticmethod
    def get_by_id(id):
        return Student.query.get(id)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
