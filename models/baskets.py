from app import db
from models.base import BaseModel

class BasketModel(db.Model, BaseModel):
    __tablename__ = 'baskets'
    #! foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)

    #! relationships
    #? many to one
    users = db.relationship('UserModel', back_populates='baskets')

    #? many to many
    products = db.relationship("BasketItemModel", back_populates="basket")