from app import ma
from models.comments import CommentModel

class CommentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CommentModel
        load_instance = True