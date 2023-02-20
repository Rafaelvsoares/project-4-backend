from marshmallow import fields
from app import ma
from models.basket_item import BasketItemModel

class BasketItemSchema1(ma.SQLAlchemyAutoSchema):
    product = fields.Nested("Product_CommentSchema")
    class Meta:
        include_fk = True
        model = BasketItemModel
        load_instance = True