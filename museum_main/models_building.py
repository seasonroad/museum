from museum_main import app, db
from museum_main.models_imgs import *


class Village(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_cn = db.Column(db.String(128))
    desc = db.Column(db.Text)
    cover_pic_id = db.Column(db.Integer)

    def __init__(self, name, desc):
        self.name_cn = name
        self.desc = desc

    @property
    def cover_pic(self):
        if self.cover_pic_id:
            return BuildingImg.query()

    @property
    def cover_pic_src(self):
        if self.cover_pic_id:
            img = BuildingImg.query.get(self.cover_pic_id)
            return os.path.relpath(img.file_path_thumb, app.config['STATIC_PRE'])


class Building(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_cn = db.Column(db.String(128))

    village_id = db.Column(db.Integer, db.ForeignKey('village.id'))
    village = db.relationship('Village', backref=db.backref('buildings', order_by=id))

    def __init__(self, name):
        pass


class Dwelling(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name_cn = db.Column(db.String(128))
    desc = db.Column(db.Text)

    village_id = db.Column(db.Integer, db.ForeignKey('village.id'))
    village = db.relationship('Village', backref=db.backref('dwelling', order_by=id))

    def __init__(self, name, desc):
        self.name_cn = name
        self.desc = desc


class Temple(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_cn = db.Column(db.String(128))
    desc = db.Column(db.Text)

    village_id = db.Column(db.Integer, db.ForeignKey('village.id'))
    village = db.relationship('Village', backref=db.backref('temple', order_by=id))

    def __init__(self, name, desc):
        self.name_cn = name
        self.desc = desc


class Tomb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_cn = db.Column(db.String(128))
    desc = db.Column(db.Text)

    village_id = db.Column(db.Integer, db.ForeignKey('village.id'))
    village = db.relationship('Village', backref=db.backref('tomb', order_by=id))

    def __init__(self, name, desc):
        self.name_cn = name
        self.desc = desc