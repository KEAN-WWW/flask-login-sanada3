from application import init_app
from application.database import db

app = init_app()

with app.app_context():
    db.create_all()
    print("Database tables created successfully!")