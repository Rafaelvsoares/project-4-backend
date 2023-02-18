from app import db
from models.base import BaseModel
from models.users import UserModel

class CommentModel(db.Model, BaseModel):
    __tablename__ = 'comments'
    content = db.Column(db.Text, nullable=False)

    #! foreign keys
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    #! relationships
    #? many to one
    products = db.relationship('ProductModel', back_populates='comments')
    users = db.relationship('UserModel', back_populates='comments')
