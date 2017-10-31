from flask import Flask
from my_app import app

app = Flask(__name__)
DEBUG = True
#TESTING = True
#app.config.from_object(__name__)
#app.config.from_pyfile('/path/to/config/file')

#app.config.from_object('configuration.DevelopmentConfig')

if __name__ == '__main__':
    app.run()