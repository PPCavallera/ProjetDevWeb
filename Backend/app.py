from flask import Flask, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_session import Session
 
app = Flask(__name__)
# creates SQLALCHEMY object

# database name
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ChatIDA.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = '32ae27c05edc697a862620724f676cbb0f4957e84e3ae4409a3228233b3e615a'
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "sqlalchemy"
db = SQLAlchemy(app)
Session(app)

@app.route('/api/response')
def test():
    print(request.args.get('question'))
    return "test réponse"

# Database ORMs
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)

@app.route("/login", methods=['POST'])
def login():
    auth = request.get_json()
    user = User.query.filter_by(email=auth['email']).first()
    if user is None:
        return {"message": "User does not exist"}, 404
    if check_password_hash(user.password, auth["password"]):
        session["name"] = user.email
        return {"isConnected": True}
    else:
        return {"message": "Incorrect password"}, 401

@app.route("/register", methods=['POST'])
def register():
    user_data = request.get_json()
    isExisting = User.query.filter_by(email=user_data['email']).first()
    if isExisting is None:
        password_hashed = generate_password_hash(user_data['password'])
        new_user = User(email=user_data['email'], password=password_hashed)
        db.session.add(new_user)
        db.session.commit()
        return {"message": "User added successfully"}, 201
    else:
        return {"message": "User already exists"}, 409

if __name__ == '__main__':
    app.run(port=5000, debug=False)