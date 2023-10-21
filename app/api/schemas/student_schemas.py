from utils import ma


class StudentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'surname', 'birthdate', 'photo')
