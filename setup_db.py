# setup_db.py
from app import app
from extensions import db
from models.user import User  # Make sure all models are imported!

with app.app_context():
    db.create_all()
    print("✅ Tables created successfully")
