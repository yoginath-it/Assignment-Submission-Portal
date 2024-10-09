from flask import Flask
from routes.admin import admin_bp
from routes.user import user_bp
from database import mongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/assignment_portal" 

# Initialize MongoDB connection
mongo.init_app(app)

# Register Blueprints
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(admin_bp, url_prefix='/admin')

if __name__ == '__main__':
    app.run(debug=True)
