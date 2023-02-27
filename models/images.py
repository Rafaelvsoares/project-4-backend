from app import db
from models.base import BaseModel

class ImageModel(db.Model, BaseModel):
    __tablename__ = "images"
    image_url = db.Column(db.Text, nullable=False)

    #! foreign keys
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False, unique=False)

    #! relationships
    #? many to one
    products = db.relationship('ProductModel', back_populates='images')
