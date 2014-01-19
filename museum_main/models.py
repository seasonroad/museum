from museum_main import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)


class Country(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name_en = db.Column(db.String(64), index = True, unique = True)
    name_cn = db.Column(db.String(128), index = True, unique = True)


class Dynasty(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name_en = db.Column(db.String(64), index = True)
    name_cn = db.Column(db.String(128), index = True)


class ReignTitle(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name_en = db.Column(db.String(64), index = True)
    name_cn = db.Column(db.String(128), index = True)


class Emperor(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name_en = db.Column(db.String(64), index = True)
    name_cn = db.Column(db.String(128), index = True)


class FamilyName(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    family_name_en = db.Column(db.String(64), index = True)
    family_name_cn = db.Column(db.String(64), index = True)
