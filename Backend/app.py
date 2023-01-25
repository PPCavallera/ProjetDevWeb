from flask import Flask, request
import pandas as pd

app = Flask(__name__)
app.config['TEMPLATE_AUTO_RELOAD'] = True


@app.route('/api/response')
def test():
    print(request.args.get('question'))
    return "test réponse"


if __name__ == '__main__':
    app.run(port=5000, debug=False)
