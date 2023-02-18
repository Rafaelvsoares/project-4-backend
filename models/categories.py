from app import db
from models.base import BaseModel

class CategoryModel(db.Model, BaseModel):

    __tablename__ = "categories"
    
    category = db.Column(db.Text, nullable=False, unique=True)

    #! relationships
    #? one to many
    products = db.relationship('ProductModel', back_populates='categories')