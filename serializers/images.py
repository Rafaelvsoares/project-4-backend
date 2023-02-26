from app import ma
from models.images import ImageModel


class ImageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        include_fk = True
        model = ImageModel
        load_instance = True
