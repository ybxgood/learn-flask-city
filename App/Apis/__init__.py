from flask_restful import Api

from App.Apis.cityResource import Hello, Provice

api = Api()

def init_api(app):
    api.init_app(app)


api.add_resource(Hello,'/hello/')
api.add_resource(Provice,'/city/')









