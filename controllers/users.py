from http import HTTPStatus
from flask import Blueprint, request
from marshmallow.exceptions import ValidationError
from models.users import UserModel
from serializers.users import UserSchema
from middleware.secure_route import secure_route


user_schema = UserSchema()

router = Blueprint('users', __name__)

@router.route('/users', methods=['GET'])
@secure_route
def get_users():
    users = UserModel.query.all()
    return user_schema.jsonify(users, many=True)

@router.route('/signup', methods=['POST'])
def signup():
    user_details = request.json

    try:
        user = user_schema.load(user_details)
        user.save()
    except ValidationError as e:
        return { "errors": e.messages, "messages": "Something went wrong..."}
    return user_schema.jsonify(user)

@router.route('/login', methods=['POST'])
def login():
    user_details = request.json
    user = UserModel.query.filter_by(email=user_details["email"]).first()
    if not user:
        return { "message": "Your email or password was incorrect." }, HTTPStatus.UNAUTHORIZED
    if not user.validate_password(user_details["password"]):
        return { "message": "Your email or password was incorrect." }, HTTPStatus.UNAUTHORIZED

    token = user.generate_token()

    return { "token": token, "message": "Welcome back!" }