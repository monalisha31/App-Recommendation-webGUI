import flask
import numpy as np
from flask import Flask
from flask import render_template
import pandas as pd
from pandas import read_csv, DataFrame
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


app = flask.Flask(__name__, template_folder='templates')
data = read_csv(r'googleplaystore.csv')
all_names = [data['App'][i] for i in range(len(data['App']))]
tfidf = TfidfVectorizer(stop_words='english')
data['Genres'] = data['Genres'].fillna('')
tfidf_matrix = tfidf.fit_transform(data['Genres'])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
indices = pd.Series(data.index, index=data['App']).drop_duplicates()


def get_recommendations(App, cosine_sim=cosine_sim):
    idx = indices[App]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    app_indices = [i[0] for i in sim_scores]
    return data['App'].iloc[app_indices]

@app.route('/', methods=['GET', 'POST'])

def main():
    if flask.request.method == 'GET':
        return(flask.render_template('index.html'))
            
    if flask.request.method == 'POST':
        a_name = flask.request.form['app_name']
        if a_name not in all_names:
            return(flask.render_template('negative.html',name=a_name))
        else:
            result_final = get_recommendations(a_name)
            names = []
            
            for i in range(len(result_final)):
                names.append(result_final.iloc[i])
              

            return flask.render_template('positive.html',app_names=names,search_name=a_name)


if __name__ == '__main__':
    app.run()

