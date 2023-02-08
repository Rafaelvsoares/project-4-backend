
from flask import Blueprint, request
from marshmallow.exceptions import ValidationError
from models.product import ProductModel
from serializers.product import ProductSchema
from serializers.comment import CommentSchema
from models.comment import CommentModel 

comment_schema = CommentSchema()
store_schema = ProductSchema()
router = Blueprint("comments", __name__)

##! Get all comments
@router.route("/comments", methods=["GET"])
def get_comments():
    comments = CommentModel.query.all()
    return comment_schema.jsonify(comments, many=True)

##! Get all comments with related ID
@router.route("/products/<int:productId>/comments", methods=["GET"])
def get_related_comments(productId):
    comments = CommentModel.query.filter_by(product_id=productId)
    return comment_schema.jsonify(comments, many=True)

##! Post product by ID
@router.route("/products/<int:productId>/comments", methods=["POST"])
def post_comment(productId):
    check_product = ProductModel.query.get(productId)
    if not check_product:
        return { "message": "The ID provided doesn't exist..." }
    try:
        comment_req = request.json
        comment = comment_schema.load(comment_req)
        comment.product_id = productId
        comment.save()
    except ValidationError as e:
        return { "errors" : e.messages, "message": "Something went wrong" }
    return comment_schema.jsonify(comment)

##! Update comment
@router.route("/products/comments/<int:commentId>", methods=["PUT"])
def update_comment(commentId):
    comment_req = request.json
    comment = CommentModel.query.get(commentId)
    if not comment:
        return { "message": "Comment ID not found..." }
    try:
        updated_comment = comment_schema.load(comment_req, instance=comment, partial=True)
        updated_comment.save()
    except ValidationError as e:
        return { "errors" : e.messages, "message": "Something went wrong" }
    return comment_schema.jsonify(comment)