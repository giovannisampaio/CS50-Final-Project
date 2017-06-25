from flask import Flask
from flask import g
import sqlite3

DATABASE = '/app.db'

def  get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

app = Flask(__name__)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def main():
    return "Hello, World!"

if __name__ == "__main__":
    app.run()

