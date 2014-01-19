from museum_main import db
from museum_main.models_building import *

class BuildingImg(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128))
    desc = db.Column(db.String(256))
    file_path_thumb = db.Column(db.String(256))
    file_path_ori = db.Column(db.String(256))

    village_id = db.Column(db.Integer, db.ForeignKey('village.id'))
    village = db.relationship('Village', backref=db.backref('images', order_by=id))

    dwelling_id = db.Column(db.Integer, db.ForeignKey('dwelling.id'))
    dwelling = db.relationship('Dwelling', backref=db.backref('images', order_by=id))

    temple_id = db.Column(db.Integer, db.ForeignKey('temple.id'))
    temple = db.relationship('Temple', backref=db.backref('images', order_by=id))

    tomb_id = db.Column(db.Integer, db.ForeignKey('tomb.id'))
    tomb = db.relationship('Tomb', backref=db.backref('images', order_by=id))


    def __init__(self, name=None, desc=None):
        self.name = name
        self.desc = desc


class PlantImg(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128))
    desc = db.Column(db.String(256))
    file_path_thumb = db.Column(db.String(256))
    file_path_ori = db.Column(db.String(256))