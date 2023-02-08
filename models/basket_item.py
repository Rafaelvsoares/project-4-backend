from app import db
from models.base import BaseModel
from models.basket import BasketModel

class BasketItemModel(db.Model, BaseModel):
    __tablename__ = "basket_item"
    quantity = db.Column(db.Integer, nullable=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    basket_id = db.Column(db.Integer, db.ForeignKey('baskets.id'))

    product = db.relationship("ProductModel", back_populates="baskets")
    
    basket = db.relationship("BasketModel", back_populates="products")