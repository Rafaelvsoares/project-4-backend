from app import db
from models.base import BaseModel

class BasketModel(db.Model, BaseModel):
    __tablename__ = 'baskets'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)
    
    products = db.relationship("BasketItemModel", back_populates="basket")