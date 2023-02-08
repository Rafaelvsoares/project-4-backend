from marshmallow import fields
from app import ma
from models.basket_item import BasketItemModel

class BasketItemSchema(ma.SQLAlchemyAutoSchema):

    product = fields.Nested("ProductSchema")
    class Meta:
        include_fk = True
        model = BasketItemModel
        load_instance = True