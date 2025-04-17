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

def std_date(article):
    '''
    gives a standard date to compare the dates between different dates

    Args:
        - date ([year, month, day]): the date an article was released
    '''
    date = get_article_date(article)
    return date[0] + (date[1] - 1)/12 + (date[2] - 1)/310

def sort_articles(articles, ascending):
    '''
    sorts the articles given

    Args:
        -  articles (list of dicts): the articles that will be 
        - ascending (bool): the order the articles will be listed as
    '''
    if len(articles) <= 1:
        return articles

    pivot = articles[len(articles) // 2]

    greater = [article for article in articles if std_date(article) > std_date(pivot)]
    equal = [article for article in articles if std_date(article) == std_date(pivot)]
    lesser = [article for article in articles if std_date(article) < std_date(pivot)]

    if ascending:
        return sort_articles(lesser, ascending) + equal + sort_articles(greater, ascending)
    # else:
    return sort_articles(greater, ascending) + equal + sort_articles(lesser, ascending)


# --------------------
# PUBLIC FUNCTIONS
# --------------------
def add_article(article):
    '''
    adds an article to 'data/articles/' with the content of it
    adds the data of the article to articles.json

    Args:
        - article (dict); with keys below
            - content (string): the content to put in the md file with title.md
            - title (string): the title of the md file
            - author (string): the user who made this
            - date ([year, month, day]): date when added
    '''
    data = load_json()

    metadata = {
        "title": article["title"],
        "author": article["author"],
        "date_created": article["date"],
        "date_edited": article["date"],
        "num": len(data),
        "archived": False
    }

    save_md(article["content"], article["title"])

    swapped = False
    for index, value in enumerate(data):
        if value is None:
            metadata["num"] = index
            data[index] = metadata
            swapped = True
            break

    if not swapped:
        data.append(metadata)

    save_json(data)

def edit_article(num, date, content):
    '''
    changes the content of title.md, and the edited date of the artilce in articles.json

    Args:
        - num (int): the articles position in data
        - date ([year, month, day]): the date that the changes happened
        - content (string): updated content
    '''
    data = load_json()

    if num >= len(data):
        return False

    data[num]["date_edited"] = date

    save_md(content, data[num]["title"])
    save_json(data)

    return True

def set_article_to(num, value):
    '''
    based on bool, changes the article at num in data to archived or not

    Args:
        - num (int): the article position in data
        - value (boolean): True = archived, False = not archived
    '''
    data = load_json()

    if num >= len(data):
        return False

    data[num]["archived"] = value

    save_json(data)

    return True

def delete_article(num):
    '''
    deletes the article at num location and replaces it in data
    deletes the article from the articles file

    Args:
        - num (int): the article to delete and replace with None
    '''

    data = load_json()

    if num >= len(data):
        return False

    article_path = os.path.join(ARTICLES_PATH, f"{data[num]['title']}.md")
    os.remove(article_path)

    data[num] = None
    save_json(data)

    return True

# functions to add
# - load_articles(articles)
# - load_article(article)

def load_articles():
    '''
    gets 
    '''
    pass

def load_article(num):
    data = load_json()

    article = data[num]

    article["content"] = load_md_as_html(article["title"])

    return article

# --------------------
# GETTER / SETTER
# --------------------
def get_article_date(article):
    '''
    returns the date of the article
    '''
    return article["date"]

def get_articles(articles):
    pass

# --------------------
# SETUP
# --------------------
if not os.path.exists(ARTICLES_PATH):
    os.makedirs(ARTICLES_PATH)

if not os.path.exists(ARTICLES_JSON):
    with open(ARTICLES_JSON, "w", encoding="utf-8") as f:
        json.dump([], f, indent=4)
