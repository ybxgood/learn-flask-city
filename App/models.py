from App.ext import model




class Provice(model.Model):
    pid = model.Column(model.Integer,primary_key=True,autoincrement=True)
    name = model.Column(model.String(32))
    cities = model.relationship('City',backref='Provice',lazy='dynamic')



class City(model.Model):
    cid = model.Column(model.Integer,primary_key=True,autoincrement=True)
    name = model.Column(model.String(32))
    provice = model.Column(model.Integer,model.ForeignKey(Provice.pid))
    villages = model.relationship('Village', backref='City', lazy='dynamic')


class Village(model.Model):
    vid = model.Column(model.Integer, primary_key=True, autoincrement=True)
    name = model.Column(model.String(32))
    city = model.Column(model.Integer, model.ForeignKey(City.cid))




