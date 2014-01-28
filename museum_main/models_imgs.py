from museum_main import app, db
from museum_main.models_building import *
import PIL.Image
import os
from StringIO import StringIO

class BuildingImg(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128))
    desc = db.Column(db.String(256))
    file_path_thumb = db.Column(db.String(256))
    file_path_ori = db.Column(db.String(256))
    size = db.Column(db.Integer)

    village_id = db.Column(db.Integer, db.ForeignKey('village.id'))
    village = db.relationship('Village', backref=db.backref('images', order_by=id))

    dwelling_id = db.Column(db.Integer, db.ForeignKey('dwelling.id'))
    dwelling = db.relationship('Dwelling', backref=db.backref('images', order_by=id))

    temple_id = db.Column(db.Integer, db.ForeignKey('temple.id'))
    temple = db.relationship('Temple', backref=db.backref('images', order_by=id))

    tomb_id = db.Column(db.Integer, db.ForeignKey('tomb.id'))
    tomb = db.relationship('Tomb', backref=db.backref('images', order_by=id))


    def __init__(self, name=None, desc=None, save_path=None, thumb_path=None):
        self.name = name
        self.desc = desc
        self.file_path_ori = save_path
        self.file_path_thumb = thumb_path

    def save(self, req_f):
        if req_f:
            req_f.save(self.file_path_ori)

    def save_thumb(self):
        img_f = PIL.Image.open(self.file_path_ori)
        img_f.thumbnail((140,140),PIL.Image.ANTIALIAS)
        img_f.save(self.file_path_thumb)

    @property
    def size(self):
        if self.file_path_ori:
            return os.path.getsize(self.file_path_ori)
        else:
            return 0

class PlantImg(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128))
    desc = db.Column(db.String(256))
    file_path_thumb = db.Column(db.String(256))
    file_path_ori = db.Column(db.String(256))