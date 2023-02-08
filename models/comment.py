from app import db
from models.base import BaseModel

class CommentModel(db.Model, BaseModel):
    __tablename__ = 'comments'
    content = db.Column(db.Text, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    products = db.relationship('ProductModel', back_populates='comments')
