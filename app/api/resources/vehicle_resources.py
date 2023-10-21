from flask import request
from flask_restful import Resource,Api
from .. import api
from ..models.vehicle_models import Vehicle
from ..schemas.vehicle_schemas import VehicleSchema

api_vehicle = Api(api)

class VehicleResource(Resource):

        def get(self):
            data = Vehicle.get_all()
            schema = VehicleSchema(many=True)

            context = {
                'status':True,
                'message':'lista de vehiculos',
                'content':schema.dump(data)
            }
            return context

        def post(self):
            try:
                data = request.get_json()

                vehicle = Vehicle()
                vehicle.license = data['license']
                vehicle.driver = data['driver']
                vehicle.save()

                schema = VehicleSchema()
                return {
                    'status':True,
                    'content':schema.dump(vehicle)
                }

            except Exception as e:
                return {
                    'status':False,
                    'message':str(e)
                },500