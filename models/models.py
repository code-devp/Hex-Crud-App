import datetime
from micawber import parse_html
from peewee import *

from app import db


class Hexagon(db.Model):
    name = db.Column(db.Integer, primary_key=True)
    neighbor = db.Column(db.String(80))
    border = db.Column(db.Integer)
    timestamp = DateTimeField(default=datetime.datetime.now)
    #
    # def __init__(self, border, neighbor):
    #     self.id = id
    #     self.neighbor = neighbor

    # @classmethod
    # def public(cls):
    #     return (Hexagon
    #             .select()
    #             .order_by(Hexagon.timestamp.desc()))
