from flask import  request, jsonify
from models import db, User



# to create a new user
@route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User()
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User has been created'}), 201