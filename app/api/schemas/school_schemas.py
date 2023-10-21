from utils import ma


class SchoolSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')