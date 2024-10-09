from werkzeug.security import generate_password_hash, check_password_hash
from database import mongo
import datetime

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = generate_password_hash(password)
        self.role = role

    def save(self):
        mongo.db.users.insert_one(self.__dict__)

    @staticmethod
    def find_by_username(username):
        return mongo.db.users.find_one({"username": username})

    @staticmethod
    def verify_password(hashed_password, password):
        return check_password_hash(hashed_password, password)


class Assignment:
    def __init__(self, userId, task, admin):
        self.userId = userId
        self.task = task
        self.admin = admin
        self.created_at = datetime.datetime.utcnow()

    def save(self):
        mongo.db.assignments.insert_one(self.__dict__)
