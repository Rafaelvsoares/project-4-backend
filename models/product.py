from app import db
from models.base import BaseModel
from models.comment import CommentModel
from models.basket_item import BasketItemModel

class ProductModel(db.Model, BaseModel):

    __tablename__ = "products"

    name = db.Column(db.Text, nullable=False, unique=True)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    volume = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text, nullable=False)

    comments = db.relationship('CommentModel', back_populates='products')

    baskets = db.relationship("BasketItemModel", back_populates="product")