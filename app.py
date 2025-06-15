from flask import Flask
from config import Config
from extensions import db, bcrypt, jwt
from routes.auth import auth_bp

app = Flask(__name__)
app.config.from_object(Config)

# Init extensions
db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

# Register blueprints
app.register_blueprint(auth_bp, url_prefix="/api/auth")

if __name__ == "__main__":
    app.run(debug=True)
