from flask import Blueprint,  request

app_resp = Blueprint('response',__name__)

@app_resp.route('/api/response')
def getResponse():
    print(request.args.get('question'))
    return "test réponse"