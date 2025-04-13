'''
articles.py is used to handle articles and data regarding the articles
'''

# --------------------
# IMPORTS
# --------------------
import os
import json
import markdown

# --------------------
# CONSTANTS
# --------------------
ARTICLES_JSON = "data/articles.json"
ARTICLES_PATH = "data/articles/"

# --------------------
# PRIVATE FUNCTIONS
# --------------------
def load_json():
    '''
    Loads the data from articles.json.

    Returns:
        - data (list): The data in articles.json
    '''
    with open(ARTICLES_JSON, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data

def save_json(data):
    '''
    Saves data into articles.json.

    Args:
        - data (list): The updated list of article metadata

    Returns:
        - bool: True if saved successfully
    '''
    with open(ARTICLES_JSON, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)
    return True

def load_md_as_html(title):
    '''
    Loads the content in title.md as HTML.

    Args:
        - title (str): The title of the article (filename without extension)

    Returns:
        - html (str or None): The content in the md file as HTML or None if not found
    '''
    article_path = os.path.join(ARTICLES_PATH, f"{title}.md")
    try:
        with open(article_path, "r", encoding="utf-8") as md_file:
            content = md_file.read()
            html = markdown.markdown(content)
        return html
    except FileNotFoundError:
        return None

def save_md(content, title):
    '''
    Saves content into title.md.

    Args:
        - content (str): The content to store in the md file
        - title (str): The title of the article (filename without extension)

    Returns:
        - bool: True if saved successfully
    '''
    article_path = os.path.join(ARTICLES_PATH, f"{title}.md")
    with open(article_path, "w", encoding="utf-8") as md_file:
        md_file.write(content)
    return True

# --------------------
# PUBLIC FUNCTIONS
# --------------------
# You can add helpers here like: get_all_articles(), add_article(), delete_article(), etc.

# --------------------
# SETUP
# --------------------
if not os.path.exists(ARTICLES_PATH):
    os.makedirs(ARTICLES_PATH)

if not os.path.exists(ARTICLES_JSON):
    with open(ARTICLES_JSON, "w", encoding="utf-8") as f:
        json.dump([], f, indent=4)
