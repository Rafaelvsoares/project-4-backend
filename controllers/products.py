from flask import Blueprint, request, g
from marshmallow.exceptions import ValidationError
from models.products import ProductModel
from serializers.products import Product_CommentSchema
from middleware.secure_route import secure_route
from http import HTTPStatus

product_schema = Product_CommentSchema()
router = Blueprint('products', __name__)

## ! Get all products (GET)
@router.route("/products", methods=["GET"])
def get_products():
    products = ProductModel.query.all()
    return product_schema.jsonify(products, many=True)

## ! Get product by ID (GET)
@router.route("/products/<int:product_id>", methods=["GET"])
def get_single_product(product_id):
    product = ProductModel.query.get(product_id)
    return product_schema.jsonify(product)

## ! Add new product (POST)
@router.route("/products", methods=["POST"])
@secure_route
def add_product():
    product_dict = request.json
    try:
        product_dict["user_id"] = g.current_user.id
        product = product_schema.load(product_dict)
        product.save()
    except ValidationError as e:
        return { "errors" : e.messages, "message": "Something went wrong" }, HTTPStatus.BAD_REQUEST
    return product_schema.jsonify(product), HTTPStatus.CREATED

# ! Delete product by ID (DELETE)
@router.route("/products/<int:product_id>", methods=["DELETE"])
@secure_route
def delete_by_id(product_id):
    product = ProductModel.query.get(product_id)
    try:
        if product is None:
            return { "message": "Product ID does not exist" }, HTTPStatus.NOT_FOUND
        if product.user_id != g.current_user.id:
            return { "message": "Unauthorized" }, HTTPStatus.UNAUTHORIZED
        product.delete()
    except ValidationError as e:
        return { "errors" : e.messages, "message": "Something went wrong" }, HTTPStatus.BAD_REQUEST
    return {"message": "product deleted"}, HTTPStatus.OK

# ! Update product by ID (PUT/PATCH)
@router.route("/products/<int:product_id>", methods=["PUT"])
@secure_route
def update_product(product_id):
    product_dict = request.json
    product = ProductModel.query.get(product_id)

    if not product:
        return { "message": "Product ID does not exist" }, HTTPStatus.NOT_FOUND
    
    if product.user_id != g.current_user.id:
        return { "message": "Unauthorized" }, HTTPStatus.UNAUTHORIZED
    
    try:
        updated_product = product_schema.load(product_dict, instance=product, partial=True)
    
    except ValidationError as e:
        return { "errors" : e.messages, "message": "Something went wrong" }, HTTPStatus.BAD_REQUEST
    
    updated_product.save()
    return product_schema.jsonify(updated_product), HTTPStatus.OK