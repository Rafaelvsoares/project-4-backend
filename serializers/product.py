from marshmallow import fields
from app import ma
from models.product import ProductModel
from serializers.comment import CommentSchema


class ProductSchema(ma.SQLAlchemyAutoSchema):
    comments = fields.Nested('CommentSchema', many=True)
    class Meta:
        model = ProductModel
        load_instance = True