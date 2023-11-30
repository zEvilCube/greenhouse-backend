from flask import Blueprint

from routers import api

blueprints: list[Blueprint] = [
    api.blueprint
]
