'''
app.py runs the website and contains all the routes and views that will be shown
'''
# --------------------
# IMPORTS
# --------------------
from os import path, makedirs

from flask import Flask, render_template

import articles

# --------------------
# CONSTANTS
# --------------------
app = Flask(__name__)

# --------------------
# ROUTES
# --------------------
@app.errorhandler(400)
@app.errorhandler(403)
@app.errorhandler(404)
@app.errorhandler(500)
def error(e):
    '''
    Handles the most common wesite errors

    Args:
        e (the error): the error which will contain the name, the code, and the description
    
    Returns:
        Error
    '''
    # Todo: error.html
    return render_template("error.html", error=e), e.code

@app.route('/')
@app.route('/articles/')
def articles_page():
    return "articles page"

@app.route('/articles/<int:num>')
def aritcle(num):
    article = articles.load_article(num)
    #check archived
    return render_template("article.html", article=article)

# --------------------
# DEPLOYMENT
# --------------------
if __name__ == "__main__":
    if not path.exists("data/articles/"):
        makedirs("data/articles")

    app.run(debug=True)
