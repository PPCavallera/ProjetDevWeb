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

tab = []
for i in pd.unique(df.genre):
    for k in i.split(','):
        tab.append(k)
genres = list(set(tab))
genres.sort()


def filter(genre, artiste, trier_par):

    return df[(df['genre'].str.contains(genre, case=False) if len(genre) > 0 else [True for i in range(len(df))]) & (
        df['artist_name'].str.contains(artiste, case=False) if len(artiste) > 0 else [True for i in range(len(df))])].sort_values(trier_par).head(LIMIT_SIZE).to_dict('records') if trier_par != 'undefined' else df[(df['genre'].str.contains(genre, case=False) if len(genre) > 0 else [True for i in range(len(df))]) & (
            df['artist_name'].str.contains(artiste, case=False) if len(artiste) > 0 else [True for i in range(len(df))])].head(LIMIT_SIZE).to_dict('records')


@app.route('/ex1')
def render1():
    return render_template('exercice1.html')


@app.route('/ex2')
def render2():
    return render_template('exercice2.html', genres=genres)


@app.route('/ex3')
def render3():
    return render_template('exercice3.html')


@app.route('/api/filter')
def filter_df():
    args = request.args
    return filter(args['genre'], args['artiste'], args['trier_par'])


@app.route('/api/plot/img')
def plot_popularity_img():
    art = request.args['artiste']
    dic = {}
    for col in ['tempo', 'key', 'time_signature', 'mode']:
        img = BytesIO()
        fig = px.histogram(df[df['artist_name'].str.contains(
            art, case=False)], x=col, color='genre')
        fig.write_image(img, format='png')
        img.seek(0)
        dic[col] = b64encode(img.getvalue()).decode('utf-8')

    return b64encode(img.getvalue()).decode('utf-8')


@app.route('/api/plot/data')
def plot_popularity_data():
    art = request.args['artiste']
    dic = {}
    for col in ['tempo', 'key', 'time_signature', 'mode']:
        fig = px.histogram(df[df['artist_name'].str.contains(
            art, case=False)], x=col, color='genre')
        dic[col] = fig.to_json()
    return dic


if __name__ == '__main__':
    app.run(port=5000, debug=True)
