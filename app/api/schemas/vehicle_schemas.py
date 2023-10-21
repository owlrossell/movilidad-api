from utils import ma


class VehicleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'license', 'driver')
