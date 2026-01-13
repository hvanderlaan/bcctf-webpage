from flask import Flask
from config import Config
from extensions import db
from routes import auth, main, challenge_bp, admin
from routes.user import user_bp
from models import User
from werkzeug.security import generate_password_hash

app: Flask = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(auth)
app.register_blueprint(main)
app.register_blueprint(challenge_bp)
app.register_blueprint(admin)
app.register_blueprint(user_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        if not User.query.filter_by(username="admin").first():
            admin_user: User = User(
                username="admin",
                password=generate_password_hash("admin"),
                is_admin=True
            )
            db.session.add(admin_user)
            db.session.commit()
    app.run(debug=False)
