from flask import Blueprint, request, jsonify
from models import User, Assignment
from database import mongo

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"message": "Username and password are required!"}), 400
    print("im yoginath")
    existing_user = User.find_by_username(data['username'])
    if existing_user:
        return jsonify({"message": "Username already exists!"}), 409
    print("hello")
    user = User(data['username'], data['password'], "user")
    print("world")
    user.save()
    return jsonify({"message": "User registered successfully!"}), 201

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    user = User.find_by_username(data['username'])
    if user and User.verify_password(user['password'], data['password']):
        return jsonify({"message": "Login successful!"}), 200
    return jsonify({"message": "Invalid credentials!"}), 401

@user_bp.route('/upload', methods=['POST'])
def upload_assignment():
    data = request.get_json()
    
    if not data or 'userId' not in data or 'task' not in data or 'admin' not in data:
        return jsonify({"message": "User ID, task, and admin are required!"}), 400

    assignment = Assignment(data['userId'], data['task'], data['admin'])
    assignment.save()
    return jsonify({"message": "Assignment uploaded successfully!"}), 201

@user_bp.route('/admins', methods=['GET'])
def fetch_admins():
    admins = list(mongo.db.users.find({"role": "admin"}))
    if not admins:
        return jsonify({"message": "No admins found."}), 404
    
    for admin in admins:
        admin["_id"] = str(admin["_id"])
    return jsonify(admins), 200