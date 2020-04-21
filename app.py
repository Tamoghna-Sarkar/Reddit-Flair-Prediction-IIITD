import pandas as pd
import flask
import pickle
import praw
import string
import nltk
import re
from nltk.corpus import stopwords
import os
import json
port = int(os.environ.get("PORT",5000))

reddit = praw.Reddit(client_id='3SYchvDH__igSg', client_secret='ZT-laFvDosSedAE_qPJ0dnkGtdA', user_agent='Scrapping Reddit_data')
subreddit = reddit.subreddit('india')
# app
model = pickle.load(open('model.pkl','rb'))
app = flask.Flask(__name__, template_folder='Templates')

#cleaning
space_symbols = re.compile('[/(){}\[\]\|@,;]')
delete_symbols = re.compile('[^0-9a-z #+_]')
STOPWORDS = set(stopwords.words('english'))

def cleaning(text):
    text = text.lower()
    text = space_symbols.sub(' ', text)
    text = delete_symbols.sub('', text)
    text = ' '.join(word for word in text.split() if word not in STOPWORDS)
    return text

def predict(url):
    url = str(url)
    submission = reddit.submission(url = url)
    abcd = {"title": [], "comments": []}
    abcd['title'] = submission.title
    submission.comments.replace_more(limit=None)
    comment = ''
    for top_level_comment in submission.comments:
      comment = comment + ' ' + top_level_comment.body
    abcd["comments"].append(comment)
    abcd = pd.DataFrame(abcd)
    abcd['title'] = abcd['title'].astype(str)
    abcd['title'] =abcd['title'].apply(cleaning)
    abcd['comments'] = abcd['comments'].astype(str)
    abcd['comments'] =abcd['comments'].apply(cleaning)
    abcd['com'] = abcd['title'] + abcd['comments']
    prediction = model.predict(abcd['title'])[0]
    return prediction

@app.route('/', methods=['GET', 'POST'])
def main():
   if flask.request.method == 'GET':
       return(flask.render_template('main.html'))
   if flask.request.method == 'POST':
       url = flask.request.form['url']
       prediction = predict(url)
       return flask.render_template('main.html', result = prediction)

"""
@app.route('/automated_testing', methods=['GET', 'POST'])
def automated_testing():

    if flask.request.method == 'GET':
        return(flask.render_template('automated_testing.html'))
    if flask.request.method == 'POST':
        my_file = flask.request.files['my_file']
        f = my_file.read()
        f = str(f,"utf-8")
        mylines = f.strip('\n')
        print(mylines)
        my = list(mylines.split('\n'))
        print(my)
        with open('qwerty.json','w') as abc:
            l = {"datas": []}
            for url in my:
                prediction = str(predict(url))
                lido = {url : prediction}
                l["datas"].append(lido)
            json.dump(l, abc)
        with open('qwerty.json','r') as xyz:
            json_object = json.load(xyz)
        return flask.render_template('automated_testing.html', result = json_object)
"""


if __name__ == '__main__':
    app.run(debug = True)
