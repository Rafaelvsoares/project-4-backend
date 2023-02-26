from marshmallow import fields
from app import ma
from models.products import ProductModel
from serializers.comments import CommentSchema
from serializers.images import ImageSchema


class Product_CommentSchema(ma.SQLAlchemyAutoSchema):
    comments = fields.Nested('CommentSchema', many=True)
    images = fields.Nested('ImageSchema', many=True)
    class Meta:
        include_fk = True
        model = ProductModel
        load_instance = True
