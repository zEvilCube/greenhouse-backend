from flask import Flask

from config import config
import database
from routers import blueprints


app = Flask(__name__)
for blueprint in blueprints:
    app.register_blueprint(blueprint)

if __name__ == "__main__":
    database.init()
    app.run(host=config.server_host.get_secret_value(), port=config.server_port.get_secret_value())
