
from flask import Blueprint, request, g
from marshmallow.exceptions import ValidationError
from models.products import ProductModel
from serializers.products import ProductSchema
from serializers.comments import CommentSchema
from models.comments import CommentModel
from middleware.secure_route import secure_route
from http import HTTPStatus

comment_schema = CommentSchema()
store_schema = ProductSchema()
router = Blueprint("comments", __name__)

# ! Get all comments
@router.route("/comments", methods=["GET"])
def get_comments():
    comments = CommentModel.query.all()
    return comment_schema.jsonify(comments, many=True)

# ! Get all comments with related ID
@router.route("/products/<int:productId>/comments", methods=["GET"])
def get_related_comments(productId):
    comments = CommentModel.query.filter_by(product_id=productId)
    return comment_schema.jsonify(comments, many=True)

# ! Post product by ID (POST)
@router.route("/products/<int:productId>/comments", methods=["POST"])
def post_comment(productId):
    check_product = ProductModel.query.get(productId)
    if not check_product:
        return { "message": "The ID provided doesn't exist..." }, HTTPStatus.NOT_FOUND
    try:
        comment_req = request.json
        comment = comment_schema.load(comment_req)
        comment.product_id = productId
        comment.save()
    except ValidationError as e:
        return { "errors" : e.messages, "message": "Something went wrong" }, HTTPStatus.BAD_REQUEST
    return comment_schema.jsonify(comment)

# ! Update comment (PUT)
@router.route("/products/comments/<int:commentId>", methods=["PUT"])
@secure_route
def update_comment(commentId):
    comment_req = request.json
    comment = CommentModel.query.get(commentId)
    if not comment:
        return { "message": "Comment ID not found..." }, HTTPStatus.NOT_FOUND
    try:
        updated_comment = comment_schema.load(comment_req, instance=comment, partial=True)
        updated_comment.save()
    except ValidationError as e:
        return { "errors" : e.messages, "message": "Something went wrong" }, HTTPStatus.BAD_REQUEST
    return comment_schema.jsonify(comment)

# ! Delete comment (DELETE)
@router.route('/products/comments/<int:commentId>', methods=["DELETE"])
@secure_route
def delete_comment(commentId):
    comment = CommentModel.query.get(commentId)
    try:
        if not comment:
            return {"message": "Comment not found"}, HTTPStatus.NOT_FOUND
        if comment.user_id != g.current_user.id:
            return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED
        comment.delete()
    except ValidationError as e:
        return {"errors": e.messages, "messages": "Something went wrong"}
    return {"message": "Comment deleted"}, HTTPStatus.OK