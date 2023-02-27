from app import ma
from marshmallow import fields
from models.products import ProductModel


class ProductSchema(ma.SQLAlchemyAutoSchema):
    images = fields.Nested('ImageSchema', many=True)
    class Meta:
        include_fk = True
        model = ProductModel
        load_instance = True