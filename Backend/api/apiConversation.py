from flask import Blueprint, session, request, session

app_conv = Blueprint('conversations',__name__)

@app_conv.route('/api/conversations')
def getConversations():
    return {"results": [{"convName": "Conv1"}, {"convName": "Conv2"}, {"convName": "Conv3"}]}