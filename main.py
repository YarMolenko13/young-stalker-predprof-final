from flask import Flask

app = Flask(__name__)


@app.get("/")
def index():
    return "index page"


if __name__ == "__main__":
    app.run(port=3000, debug=False)