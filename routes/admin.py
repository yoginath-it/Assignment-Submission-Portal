from flask import Blueprint, request, jsonify
from models import User, Assignment
from database import mongo
from bson import ObjectId

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"message": "Username and password are required!"}), 400

    existing_user = User.find_by_username(data['username'])
    if existing_user:
        return jsonify({"message": "Username already exists!"}), 409

    user = User(data['username'], data['password'], "admin")
    user.save()
    return jsonify({"message": "Admin registered successfully!"}), 201

@admin_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    user = User.find_by_username(data['username'])
    if user and User.verify_password(user['password'], data['password']):
        return jsonify({"message": "Login successful!"}), 200
    return jsonify({"message": "Invalid credentials!"}), 401

@admin_bp.route('/assignments', methods=['GET'])
def view_assignments():
    admin_name = request.args.get('admin')
    if not admin_name:
        return jsonify({"message": "Admin name is required!"}), 400

    # Fetch assignments for this admin
    assignments = list(mongo.db.assignments.find({"admin": admin_name}))

    # Convert ObjectId to string
    for assignment in assignments:
        assignment['_id'] = str(assignment['_id'])

    return jsonify(assignments), 200


@admin_bp.route('/assignments/<assignment_id>/accept', methods=['POST'])
def accept_assignment(assignment_id):
    mongo.db.assignments.update_one({"_id": assignment_id}, {"$set": {"status": "accepted"}})
    return jsonify({"message": "Assignment accepted!"}), 200

@admin_bp.route('/assignments/<assignment_id>/reject', methods=['POST'])
def reject_assignment(assignment_id):
    mongo.db.assignments.update_one({"_id": assignment_id}, {"$set": {"status": "rejected"}})
    return jsonify({"message": "Assignment rejected!"}), 200
