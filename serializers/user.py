import re
from marshmallow import fields, ValidationError
from app import ma
from models.user import UserModel
from serializers.basket import BasketSchema

def validate_password(password):
    if len(password) < 8:
        raise ValidationError("Password must at least 8 characters.")
    elif re.search("[A-Z]", password) is None:
        raise ValidationError("Password must have at least 1 capital letter.")

class UserSchema(ma.SQLAlchemyAutoSchema):
    baskets = fields.Nested('BasketSchema', many=True)
    password = fields.String(required=True, validate=validate_password)
    class Meta:
        model = UserModel
        load_instance = True
        exclude = ("password_hash",)
        load_only = ("email", "password")