from flask import Flask

import database
from routers import blueprints

app = Flask(__name__)

if __name__ == "__main__":
    database.init()
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
    app.run()
