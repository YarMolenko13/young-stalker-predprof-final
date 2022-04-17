from config import *

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = DATABASE_URL
db = SQLAlchemy(app)


@app.get("/")
def index():
    return "index page"


if __name__ == "__main__":
    app.run(port=3000, debug=False)