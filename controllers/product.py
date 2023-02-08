from flask import Blueprint, request
from marshmallow.exceptions import ValidationError
from models.product import ProductModel
from serializers.product import ProductSchema

product_schema = ProductSchema()
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
def add_product():
    product_dict = request.json
    try:
        product = product_schema.load(product_dict)
        product.save()
    except ValidationError as e:
        return { "errors" : e.messages, "message": "Something went wrong" }
    return product_schema.jsonify(product)

# ! Delete product by ID (DELETE)
@router.route("/products/<int:product_id>", methods=["DELETE"])
def delete_by_id(product_id):
    product = ProductModel.query.get(product_id)
    try:
        if product is None:
            return { "message": "ID does not exist" }
        product.delete()
    except ValidationError as e:
        return { "errors" : e.messages, "message": "Something went wrong" }
    return {"message": "product deleted"}
