from flask import Flask, render_template, request, send_file
import pandas as pd

app = Flask(__name__)
app.config['TEMPLATE_AUTO_RELOAD'] = True


@app.route('/api/test')
def test():
    return {"test": 'test'}


if __name__ == '__main__':
    app.run(port=5000, debug=False)
