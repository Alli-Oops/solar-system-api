from app import db
from dataclasses import dataclass

@dataclass
class Planet(db.Model):
    id: int
    name: str
    description: str
    color: str 

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    color = db.Column(db.String)