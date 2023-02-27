from app import db
from models.base import BaseModel
from models.comments import CommentModel
from models.basket_item import BasketItemModel
from models.images import ImageModel
from models.categories import CategoryModel

class ProductModel(db.Model, BaseModel):

    __tablename__ = "products"

    title = db.Column(db.Text, nullable=False, unique=True)
    price = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    polygons = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)

    #! foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False, unique=False)

    #! relationships
    #? one to many
    comments = db.relationship('CommentModel', back_populates='products', cascade="all, delete")
    images = db.relationship('ImageModel', back_populates='products', cascade="all, delete")
    
    #? many to one
    users = db.relationship('UserModel', back_populates='products')
    categories = db.relationship('CategoryModel', back_populates='products')

    #? many to many
    baskets = db.relationship("BasketItemModel", back_populates="product")
