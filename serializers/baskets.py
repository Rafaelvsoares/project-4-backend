from marshmallow import fields
from app import ma
from models.baskets import BasketModel
from serializers.basket_item import BasketItemSchema1

class BasketSchema(ma.SQLAlchemyAutoSchema):

    products = fields.Nested("BasketItemSchema1", many=True)

    class Meta:
        include_fk = True
        model = BasketModel
        load_instance =True