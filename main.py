from flask import Flask

from routers import blueprints

app = Flask(__name__)

if __name__ == "__main__":
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
    app.run()
