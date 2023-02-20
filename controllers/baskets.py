from flask import Blueprint, request, g
from marshmallow.exceptions import ValidationError
from models.basket_item import BasketItemModel
from models.baskets import BasketModel
from serializers.basket.basket_item import BasketItemSchema
from serializers.baskets import BasketSchema
from middleware.secure_route import secure_route
from http import HTTPStatus

basket_item_schema = BasketItemSchema()
basket_schema = BasketSchema()
router = router = Blueprint("baskets", __name__)

@router.route("/basket", methods=["GET"])
def all_baskets():
    basketItems = BasketItemModel.query.all()
    return basket_item_schema.jsonify(basketItems, many=True)

@router.route("/basket/<int:basketId>", methods=["GET"])
@secure_route
def user_basket(basketId):
    user_basket = BasketModel.query.filter_by(user_id=g.current_user.id, id=basketId)
    try:
        basket = BasketItemModel.query.filter_by(basket_id=basketId)
    except ValidationError as e:
        return { "errors" : e.messages, "message": "Something went wrong" }, HTTPStatus.BAD_REQUEST
    # return basket_item_schema.jsonify(basket, many=True)
    return basket_schema.jsonify(user_basket, many=True)