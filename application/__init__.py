from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine
from mongoengine import connect
import os

# app = Flask(__name__)
# app.config.from_object(Config)

# db = MongoEngine()
# db.init_app(app)

app = Flask(__name__)
DB_URI = "mongodb+srv://dreid254:Guinness02@cluster0-xqife.gcp.mongodb.net/my_quizzes?retryWrites=true&w=majority"
app.config["MONGODB_HOST"] = DB_URI
db = MongoEngine(app)

if __name__ == '__main__':
    app.run()
app.config.from_object(Config)

from application import routes