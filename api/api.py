# AneMo - Raspberry Pi based temperature control system
#           for home automation
# 
# Updated by Jack Spargo - 28/02/2015

from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid

if __name__ == '__main__':
    app.run(host='0.0.0.0')
