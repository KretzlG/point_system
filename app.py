from flask import Flask
from routes import bp
from db import db
from models import User

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'
app.register_blueprint(bp)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///point_system.db'
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Criação automática do usuário admin
        if not User.query.filter_by(username='GianKretzl').first():
            user = User(
                name='Gian Felipe Kretzl',
                username='GianKretzl',
                password='123456',  # Use hash em produção!
                is_admin=True,
                is_employee=False
            )
            db.session.add(user)
            db.session.commit()
    app.run(debug=True)