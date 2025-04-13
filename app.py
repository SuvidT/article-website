'''
app.py runs the website and contains all the routes and views that will be shown
'''
# --------------------
# IMPORTS
# --------------------
from flask import Flask

# --------------------
# CONSTANTS
# --------------------
app = Flask(__name__)



# --------------------
# DEPLOYMENT
# --------------------
if __name__ == "__main__":
    app.run(debug=True)
