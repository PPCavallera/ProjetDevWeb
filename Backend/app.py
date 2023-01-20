from flask import Flask, render_template, request, send_file
import sys
import plotly.express as px
from base64 import b64encode
from io import BytesIO
import plotly
import pandas as pd

LIMIT_SIZE = 20

app = Flask(__name__)
app.config['TEMPLATE_AUTO_RELOAD'] = True

# Loading dataset

df = pd.read_csv('dataset.csv')


@app.route('/api/test')
def test():
    return df.head(20).to_dict('records')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
