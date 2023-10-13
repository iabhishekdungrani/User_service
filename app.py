# user_service.py

from flask import Flask, jsonify, request

app = Flask(__name__)

    
@app.route('/')
def hello():
    return 'User serive is live!'

# Retrive user_service

@app.route('/user/<id>', methods=['GET'])
def get_user(id):
    users = {
        '1': {'name': 'Alice', 'email': 'alice@example.com'},
        '2': {'name': 'Bob', 'email': 'bob@example.com'}
    }
    user_info = users.get(id, {})
    return jsonify(user_info)

#create user_service


@app.route('/user', methods=["POST"])
def add_user():

    users = {
        '1': {'name': 'Alice', 'email': 'alice@example.com'},
        '2': {'name': 'Bob', 'email': 'bob@example.com'}
         }

    new_user = request.get_json()
    id = str(len(users) + 1)
    users[id] = new_user
    new_user["id"] = id
    return jsonify({"message": "user created", "new_user": new_user}), 201

#delete user_service.py

@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
        users = {
        '1': {'name': 'Alice', 'email': 'alice@example.com'},
        '2': {'name': 'Bob', 'email': 'bob@example.com'}
         }
        user_info = users.get(id, {})
        if user_info:
            users.pop(id)
            return jsonify({"message": "User deleted"})
        else:
            return jsonify({"error": "User not found"}), 404
    
#update user_service.py

@app.route('/user/<id>', methods=['PUT'])
def update_user(id):
    users = {
        '1': {'name': 'Alice', 'email': 'alice@example.com'},
        '2': {'name': 'Bob', 'email': 'bob@example.com'}
         }
    if id in users:
            user_info = users.get(id)
            data = request.json
            user_info['name'] = data.get('name', user_info['name'])
            user_info['email'] = data.get('email', user_info['email'] )        
        
            return jsonify({"message": "User updated", "user_info": user_info})
    else:
            return jsonify({"error": "User not found"}), 404
    

if __name__ == '_main_':
    app.run('0.0.0.0',port=5000)