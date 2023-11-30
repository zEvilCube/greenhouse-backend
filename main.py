from flask import Flask

import database
from routers import blueprints

app = Flask(__name__)
for blueprint in blueprints:
    app.register_blueprint(blueprint)

if __name__ == "__main__":
    database.init()
    app.run()
