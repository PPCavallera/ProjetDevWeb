from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
# creates SQLALCHEMY object

# database name
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ChatIDA.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config["TEMPLATES_AUTO_RELOAD"] = True
db = SQLAlchemy(app)


# Database ORMs
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(40), unique=False, nullable=False)


class Conversation(db.Model):
    conv_id = db.Column(db.Integer, primary_key=True)
    conv_name = db.Column(db.String(120))
    user_id = db.Column(db.Integer)


class Message(db.Model):
    mess_id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1027))
    conv_id = db.Column(db.Integer)


@app.route('/api/response')
def test():
    print(request.args.get('question'))
    print(request.args.get('conv_id'))
    question = Message(content=request.args.get('question'),
                       conv_id=request.args.get('conv_id'))
    answer = Message(content="test réponse",
                     conv_id=request.args.get('conv_id'))
    db.session.add(question)
    db.session.add(answer)
    db.session.commit()
    return "test réponse"


@app.route('/api/load_messages')
def loadMessages():
    print(request.args.get('conv_id'))
    messages = Message.query.filter_by(conv_id=request.args.get('conv_id'))
    res_li = []
    if messages.count() > 0:
        for i in range(0, messages.count()-1, 2):
            res_li.append(
                {'question': messages[i].content, 'answer': messages[i+1].content})
    return {"results": res_li}


@app.route('/api/conversations', methods=['GET', 'DELETE', 'POST'])
def getConversations():
    if request.method == 'GET':
        user = User.query.filter_by(username=request.args.get('user')).first()
        convs = Conversation.query.filter_by(user_id=user.user_id)
        res = {}
        res['results'] = []
        for c in convs:
            conv_dict = {}
            conv_dict['conv_id'] = c.conv_id
            conv_dict['conv_name'] = c.conv_name
            # messages = Message.query.filter_by(conv_id=c.conv_id)
            # questions = []
            # answers = []
            # for m in messages:
            #     msg_dict = {}
            #     msg_dict['mess_id'] = m.mess_id
            #     msg_dict['content'] = m.content
            #     msg_dict['position'] = m.position
            #     questions.append(msg_dict) if m.position % 2 != 0 else answers.append(msg_dict)
            # conv_dict['question'] = questions
            # conv_dict['answers'] = answers
            res['results'].append(conv_dict)
        return res
    if request.method == 'DELETE':
        messages = Message.query.filter_by(conv_id=request.args.get('conv_id')).all()
        convs = Conversation.query.filter_by(conv_id=request.args.get('conv_id')).all()
        for m in messages:
            db.session.delete(m)
            db.session.commit()
        for c in convs:
            db.session.delete(c)
            db.session.commit()
        return {'message' : "Deleted Conversation"}
    if request.method == 'POST':
        user = User.query.filter_by(username=request.args.get('user')).first()
        newConv = Conversation(conv_name=request.args.get('conv_name'), user_id=user.user_id)
        db.session.add(newConv)
        db.session.commit()
        addedConv = Conversation.query.filter_by(conv_name=request.args.get('conv_name')).first()
        return {'conv_id': addedConv.conv_id, 'conv_name': addedConv.conv_name}


@app.route("/login", methods=['POST'])
def login():
    auth = request.get_json()
    user = User.query.filter_by(username=auth['username']).first()
    if user is None:
        return {"message": "User does not exist"}, 404
    if check_password_hash(user.password, auth["password"]):
        return {"isConnected": True, "user": user.username}, 200
    else:
        return {"message": "Incorrect password"}, 401


@app.route("/register", methods=['POST'])
def register():
    user_data = request.get_json()
    isExisting = User.query.filter_by(username=user_data['username']).first()
    if isExisting is None:
        password_hashed = generate_password_hash(user_data['password'])
        new_user = User(
            username=user_data['username'], password=password_hashed)
        db.session.add(new_user)
        db.session.commit()
        return {"message": "User added successfully"}, 201
    else:
        return {"message": "User already exists"}, 409


if __name__ == '__main__':
    app.run(port=5000, debug=False)
