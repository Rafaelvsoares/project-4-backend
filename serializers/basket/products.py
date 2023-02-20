from app import ma
from models.products import ProductModel


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        include_fk = True
        model = ProductModel
        load_instance = True