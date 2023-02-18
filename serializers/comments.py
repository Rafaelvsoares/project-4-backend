from app import ma
from models.comments import CommentModel

class CommentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        include_fk = True
        model = CommentModel
        load_instance = True