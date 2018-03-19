from flask_restful import Resource, fields, marshal_with
from flask_restful.fields import Nested

from App.models import Provice, City, Village


class Hello(Resource):
    def get(self):
        return {'hello':'world'}


# vill_fields={
#     'name': fields.String,
# }
#
# city_fields={
#     'name':fields.String,
#     'area':fields.List(fields.Nested(vill_fields))
# }
#
#
# pro_fields={
#     'name':fields.String,
#     'city':fields.List(Nested(city_fields))
# }

class Provice(Resource):
    # @marshal_with(pro_fields)
    def get(self):

        data = {}
        city_fields = {}

        vill_fields = {
            'name': fields.String,
        }
        citys = City.query.all()

        for city in citys:
            print(city.name)
            city_fields['name'] = city.name
            city_fields['area'] = fields.List(fields.Nested(vill_fields))

            vills = city.villages
            print(vills)
            data['area'] = vills
            # data['city'] = fields.List(fields.Nested(city_fields))
            # data['name'] = city.provice
        result = marshal_with(data,city_fields)

        return {'data':result}









