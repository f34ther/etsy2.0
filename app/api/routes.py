from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Item, item_schema, items_schema

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/items', methods=['POST'])
@token_required
def create_item(current_user_token):
    title = request.json['title']
    description = request.json['description']
    price = request.json['price']
    shipping_id = request.json['shipping_id']
    user_token = current_user_token.token

    print(f'Test: {current_user_token}')

    item = Item(title, description, price, shipping_id, user_token=user_token)

    db.session.add(item)
    db.session.commit()

    response = item_schema.dump(item)
    return jsonify(response)


@api.route('/items', methods=['GET'])
@token_required
def get_items(current_user_token):
    a_user = current_user_token.token
    items = Item.query.filter_by(user_token=a_user).all()
    response = items_schema.dump(items)
    return jsonify(response)


@api.route('/items/id', methods=['GET'])
@token_required
def get_single_item(current_user_token, id):
    item = Item.query.get(id)
    item.user_token = current_user_token.token
    response = item_schema.dump(item)
    return jsonify(response)


@api.route('/items/<id>', methods=['PUT'])
@token_required
def update_item(current_user_token, id):
    item = Item.query.get(id)
    item.title = request.json['title']
    item.description = request.json['description']
    item.price = request.json['price']
    item.shipping_id = request.json['shipping_id']
    item.user_token = current_user_token.token

    db.session.commit()
    response = item_schema.dump(item)
    return jsonify(response)


@api.route('/items/<id>', methods=['DELETE'])
@token_required
def delete_item(current_user_token, id):
    item = Item.query.get(id)
    item.user_token = current_user_token.token
    db.session.delete(item)
    db.session.commit()
    response = item_schema.dump(item)
    return jsonify(response)
