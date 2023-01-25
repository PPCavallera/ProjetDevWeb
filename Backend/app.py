from flask import Flask, request
import pandas as pd
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# database name
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ChatIDA.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# creates SQLALCHEMY object
db = SQLAlchemy(app)


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
        return str("wrong email")
    if user.password == auth['password']:
        return str("it works")
    else:
        return str("wrong credentials")

@app.route("/register", methods=['POST'])
def register():
    user_data = request.get_json()
    
if __name__ == '__main__':
    app.run(port=5000, debug=False)
